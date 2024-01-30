# (C) Khulnasoft, Inc. 2023-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import datetime
import pprint
import threading
import time
import uuid

import psycopg2
import pytest

from khulnasoft_checks.postgres import PostgreSql
from khulnasoft_checks.postgres.connections import ConnectionPoolFullError, MultiDatabaseConnectionPool

from .common import HOST, PASSWORD_ADMIN, USER_ADMIN
from .utils import _get_superconn


@pytest.mark.integration
@pytest.mark.usefixtures('dd_environment')
def test_conn_pool(pg_instance):
    """
    Test simple case of creating a connection pool, pruning a stale connection,
    and closing all connections.
    """
    check = PostgreSql('postgres', {}, [pg_instance])

    pool = MultiDatabaseConnectionPool(check._new_connection)
    db = pool._get_connection_raw('postgres', 1)
    assert pool._stats.connection_opened == 1
    pool.prune_connections()
    assert len(pool._conns) == 1
    assert pool._stats.connection_closed == 0

    with db.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
        cursor.execute("select 1")
        rows = cursor.fetchall()
        assert len(rows) == 1 and rows[0][0] == 1

    time.sleep(0.001)
    pool.prune_connections()
    assert len(pool._conns) == 0
    assert pool._stats.connection_closed == 1
    assert pool._stats.connection_closed_failed == 0
    assert pool._stats.connection_pruned == 1

    db = pool._get_connection_raw('postgres', 999 * 1000)
    assert len(pool._conns) == 1
    assert pool._stats.connection_opened == 2
    success = pool.close_all_connections()
    assert success
    assert len(pool._conns) == 0
    assert pool._stats.connection_closed == 2
    assert pool._stats.connection_closed_failed == 0
    assert pool._stats.connection_pruned == 1


@pytest.mark.integration
@pytest.mark.usefixtures('dd_environment')
def test_conn_pool_no_leaks_on_close(pg_instance):
    """
    Test a simple case of opening and closing many connections. There should be no leaked connections on the server.
    """
    unique_id = str(uuid.uuid4())  # Used to isolate this test from others on the DB

    check = PostgreSql('postgres', {}, [pg_instance])
    check._config.application_name = unique_id

    # Used to make verification queries
    pool2 = MultiDatabaseConnectionPool(
        lambda dbname: psycopg2.connect(host=HOST, dbname=dbname, user=USER_ADMIN, password=PASSWORD_ADMIN)
    )

    # Iterate in the test many times to detect flakiness
    for _ in range(20):
        pool = MultiDatabaseConnectionPool(check._new_connection)

        def get_activity():
            """
            Fetches all pg_stat_activity rows generated by this test and connection to a "dogs%" database
            """
            with pool2.get_connection('postgres', 1) as conn:
                cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
                cursor.execute(
                    "SELECT pid, datname, usename, state, query_start, state_change, application_name"
                    " FROM pg_stat_activity"
                    " WHERE datname LIKE 'dogs%%' AND application_name = %s",
                    (unique_id,),
                )
                return cursor.fetchall()

        conn_count = 100
        for i in range(0, conn_count):
            dbname = 'dogs_{}'.format(i)
            db = pool._get_connection_raw(dbname, 10 * 1000)
            with db.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute("select current_database()")
                rows = cursor.fetchall()
                assert len(rows) == 1
                assert rows[0][0] == dbname

        assert pool._stats.connection_opened == conn_count
        assert len(get_activity()) == conn_count

        pool.close_all_connections()
        assert pool._stats.connection_closed == conn_count
        assert pool._stats.connection_closed_failed == 0

        # Ensure all the connections have been terminated on the server
        attempts = 5
        while True:
            attempts -= 1

            rows = get_activity()
            if len(rows) == 0:
                break

            assert attempts >= 0, "Connections leaked! Leaked rows found:\n{}".format(pprint.pformat(rows))
            time.sleep(1)


@pytest.mark.integration
@pytest.mark.usefixtures('dd_environment')
def test_conn_pool_no_leaks_on_prune(pg_instance):
    """
    Test a scenario where many connections are created. These connections should be open on the database
    then should properly close on the pooler side and database when pruned and/or closed.
    """
    unique_id = str(uuid.uuid4())  # Used to isolate this test from others on the DB

    check = PostgreSql('postgres', {}, [pg_instance])
    check._config.application_name = unique_id

    pool = MultiDatabaseConnectionPool(check._new_connection)
    # Used to make verification queries
    pool2 = MultiDatabaseConnectionPool(
        lambda dbname: psycopg2.connect(host=HOST, dbname=dbname, user=USER_ADMIN, password=PASSWORD_ADMIN)
    )
    ttl_long = 90 * 1000
    ttl_short = 1

    def get_activity():
        """
        Fetches all pg_stat_activity rows generated by this test and connection to a "dogs%" database
        """
        with pool2.get_connection('postgres', 1) as conn:
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cursor.execute(
                "SELECT pid, datname, usename, state, query_start, state_change, application_name"
                " FROM pg_stat_activity"
                " WHERE datname LIKE 'dogs%%' AND application_name = %s",
                (unique_id,),
            )
            return cursor.fetchall()

    def get_many_connections(count, ttl):
        """
        Retrieves the number of connections from the pool with the specified TTL
        """
        for i in range(0, count):
            dbname = 'dogs_{}'.format(i)
            db = pool._get_connection_raw(dbname, ttl)
            with db.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute("select current_database()")
                rows = cursor.fetchall()
                assert len(rows) == 1
                assert rows[0][0] == dbname

    pool.close_all_connections()

    pool._stats.reset()

    # Create many connections with long-lived TTLs
    get_many_connections(50, ttl_long)
    assert len(pool._conns) == 50
    assert pool._stats.connection_opened == 50
    # Ensure those connections have the correct deadline and connection status
    for i in range(0, 50):
        dbname = 'dogs_{}'.format(i)
        conn_info = pool._conns[dbname]
        db = conn_info.connection
        deadline = conn_info.deadline
        approximate_deadline = datetime.datetime.now() + datetime.timedelta(milliseconds=ttl_long)
        assert (
            approximate_deadline - datetime.timedelta(seconds=1)
            < deadline
            < approximate_deadline + datetime.timedelta(seconds=1)
        )
        assert not db.closed
        assert db.status == psycopg2.extensions.STATUS_READY
    # Check that those pooled connections do exist on the database
    rows = get_activity()
    assert len(rows) == 50
    assert len({row['datname'] for row in rows}) == 50
    assert all(row['state'] == 'idle' for row in rows)

    pool._stats.reset()

    # Repeat this process many times and expect that only one connection is created per database
    for _ in range(100):
        get_many_connections(51, ttl_long)
        assert pool._stats.connection_opened == 1

        attempts_to_verify = 10
        # Loop here to prevent flakiness. Sometimes postgres doesn't immediately terminate backends.
        # The test can be considered successful as long as the backend is eventually terminated.
        for attempt in range(attempts_to_verify):
            rows = get_activity()
            server_pids = {row['pid'] for row in rows}
            conns = [c.connection for c in pool._conns.values()]
            conn_pids = {db.info.backend_pid for db in conns}
            leaked_rows = [row for row in rows if row['pid'] in server_pids - conn_pids]
            if not leaked_rows:
                break
            if attempt < attempts_to_verify - 1:
                time.sleep(1)
                continue
            assert len(leaked_rows) == 0, 'Found leaked rows on the server not in the connection pool'

        assert len({row['datname'] for row in rows}) == 51
        assert len(rows) == 51, 'Possible leaked connections'
        assert all(row['state'] == 'idle' for row in rows)
    assert pool._stats.connection_opened == 1
    assert pool._stats.connection_closed == 0

    pool._stats.reset()

    # Now update db connections with short-lived TTLs and expect them to self-prune
    get_many_connections(55, ttl_short)
    time.sleep(0.001)
    pool.prune_connections()

    assert pool._stats.connection_opened == 55 - 51
    assert pool._stats.connection_closed == 55
    assert pool._stats.connection_pruned == 55
    assert pool._stats.connection_closed_failed == 0
    attempts_to_verify = 10
    for attempt in range(attempts_to_verify):
        leaked_rows = get_activity()
        if attempt < attempts_to_verify - 1:
            time.sleep(1)
            continue
        assert len(leaked_rows) == 0, 'Found leaked rows remaining after TTL was updated to short TTL'

    # Final check that the server contains no leaked connections still open
    rows = get_activity()
    assert len(rows) == 0


@pytest.mark.integration
@pytest.mark.usefixtures('dd_environment')
def test_conn_pool_single_context(pg_instance):
    """
    Test creating a single connection.
    """
    check = PostgreSql('postgres', {}, [pg_instance])

    pool = MultiDatabaseConnectionPool(check._new_connection)
    with pool.get_connection("dogs_0", 1000):
        pass

    assert pool._stats.connection_opened == 1

    expected_evicted = "dogs_0"
    evicted = pool.evict_lru()
    assert evicted == expected_evicted
    assert pool._stats.connection_closed == 1

    # ask for another connection again, error not raised
    with pool.get_connection("dogs_1", 1000):
        pass


@pytest.mark.integration
@pytest.mark.usefixtures('dd_environment')
def test_conn_pool_context_managed(pg_instance):
    """
    Test context manager API for connection grabbing.
    """

    def pretend_to_run_query(pool, dbname):
        with pool.get_connection(dbname, 10000):
            time.sleep(5)

    limit = 30
    check = PostgreSql('postgres', {}, [pg_instance])

    pool = MultiDatabaseConnectionPool(check._new_connection, limit)
    threadpool = []
    for i in range(limit):
        thread = threading.Thread(target=pretend_to_run_query, args=(pool, 'dogs_{}'.format(i)))
        threadpool.append(thread)
        thread.start()

    time.sleep(1)
    assert pool._stats.connection_opened == limit

    # ask for one more connection
    with pytest.raises(ConnectionPoolFullError):
        with pool.get_connection('dogs_{}'.format(limit + 1), 1, 1):
            pass

    # join threads
    for thread in threadpool:
        thread.join()

    # now can add a new connection, one will get kicked out of pool
    with pool.get_connection('dogs_{}'.format(limit + 1), 60000):
        pass

    assert pool._stats.connection_closed == 1

    # close the rest
    pool.close_all_connections()
    assert pool._stats.connection_closed == limit + 1


@pytest.mark.integration
@pytest.mark.usefixtures('dd_environment')
def test_conn_terminated_prematurely(pg_instance):
    """
    Test db connection terminated prematurely
    """

    def _terminate_connection(conn, dbname):
        # function to abruptly terminate a connection
        with conn.cursor() as cursor:
            print(dbname)
            cursor.execute(
                "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE pid <> pg_backend_pid() AND datname = %s",
                (dbname,),
            )

    check = PostgreSql('postgres', {}, [pg_instance])
    conn = _get_superconn(pg_instance)

    check.check(pg_instance)
    assert check._db is not None
    assert not check._db.closed

    _terminate_connection(conn, pg_instance['dbname'])
    time.sleep(1)

    assert check._db is not None

    # the connection is terminated on the server, psycopg has no way of knowing
    # this check run will fail but the connection status should be updated
    with pytest.raises(psycopg2.Error):
        check.check(pg_instance)

    # connection status is updated to closed
    assert check._db is not None
    assert check._db.closed

    # new check run will re-open connection
    check.check(pg_instance)
