#!/bin/bash
set -e

pg_ctl -D /var/lib/postgresql/data -l /tmp/logfile -w stop
rm -rf /var/lib/postgresql/data/*

echo "Testing primary"
while ! pg_isready -U datadog -d khulnasoft_test -h postgres -p 5432 ; do
    echo "Primary not running, waiting"
    sleep 1
done

echo "Running pg basebackup"
export PGPASSWORD='replicator'
pg_basebackup -h postgres -U replicator -S replication_slot -X stream -v -R -D /var/lib/postgresql/data/
echo "pg basebackup executed"

pg_ctl -D /var/lib/postgresql/data -w start
