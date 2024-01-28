# (C) Datadog, Inc. 2018-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from copy import deepcopy

import pytest
from six.moves.urllib import error
from six.moves.urllib.request import urlopen

from khulnasoft_checks.dev import WaitFor, docker_run
from khulnasoft_checks.lighttpd import Lighttpd

from . import common


def wait_for_lighttpd():
    try:
        urlopen(common.STATUS_URL).read()
    except error.HTTPError:
        # endpoint is secured, we do expect 401
        return


@pytest.fixture(scope="session")
def dd_environment():
    with docker_run(common.COMPOSE_FILE, conditions=[WaitFor(wait_for_lighttpd)], mount_logs=True):
        instance = deepcopy(common.INSTANCE)
        yield instance


@pytest.fixture
def check():
    check = Lighttpd('lighttpd', {}, [common.INSTANCE])
    return check


@pytest.fixture
def instance():
    instance = deepcopy(common.INSTANCE)
    return instance
