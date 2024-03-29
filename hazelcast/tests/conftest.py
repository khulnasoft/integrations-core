# (C) Khulnasoft, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os

import pytest
import requests

from khulnasoft_checks.dev import docker_run
from khulnasoft_checks.dev.conditions import CheckDockerLogs, WaitFor
from khulnasoft_checks.dev.utils import load_jmx_config
from khulnasoft_checks.hazelcast import HazelcastCheck

from . import common


@pytest.fixture(scope='session')
def dd_environment():
    compose_file = os.path.join(common.HERE, 'docker', 'docker-compose.yaml')
    with docker_run(
        compose_file,
        build=True,
        mount_logs=True,
        conditions=[
            CheckDockerLogs('hazelcast_management_center', ['Hazelcast Management Center successfully started']),
            CheckDockerLogs('hazelcast_management_center', ['Started communication with member']),
            CheckDockerLogs('hazelcast2', [r'Hazelcast JMX agent enabled']),
            CheckDockerLogs('hazelcast2', [r'is STARTED']),
            WaitFor(trigger_some_tcp_data),
        ],
        attempts=5,
        attempts_wait=5,
    ):
        config = load_jmx_config()
        config['instances'] = common.INSTANCE_MEMBERS + [common.INSTANCE_MC_JMX, common.INSTANCE_MC_PYTHON]
        yield config, {'use_jmx': True}


def trigger_some_tcp_data():
    base_url = 'http://{}:{}'.format(common.HOST, common.MEMBER_REST_PORT)
    for i in range(100):
        url = "{}/hazelcast/rest/maps/mapName/foo{}".format(base_url, i)
        requests.post(url, data='bar')
        resp = requests.get(url)
        assert resp.content.decode('utf-8') == 'bar'


@pytest.fixture(scope='session')
def hazelcast_check():
    return lambda instance: HazelcastCheck('hazelcast', {}, [instance])
