# (C) Khulnasoft, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import pytest
from six import PY2, PY3

from khulnasoft_checks.dev import docker_run
from khulnasoft_checks.dev.conditions import CheckDockerLogs
from khulnasoft_checks.teamcity.teamcity_rest import TeamCityRest

if PY3:
    from khulnasoft_checks.teamcity.teamcity_openmetrics import TeamCityOpenMetrics

from .common import (
    COMPOSE_FILE,
    LEGACY_REST_INSTANCE,
    METRIC_ENDPOINT,
    OPENMETRICS_INSTANCE,
    REST_INSTANCE,
    USE_OPENMETRICS,
)


@pytest.fixture(scope='session')
def dd_environment(rest_instance, openmetrics_instance):
    compose_file = COMPOSE_FILE.format('mockserver')
    instance = rest_instance
    endpoints = None
    conditions = None
    if USE_OPENMETRICS:
        compose_file = COMPOSE_FILE.format('teamcity_server')
        instance = openmetrics_instance
        endpoints = [METRIC_ENDPOINT]
        conditions = [CheckDockerLogs('teamcity-server', ['TeamCity initialized'], attempts=100, wait=3)]

    with docker_run(compose_file, endpoints=endpoints, conditions=conditions, sleep=10):
        yield instance


@pytest.fixture(scope='session')
def rest_instance():
    if PY2:
        return LEGACY_REST_INSTANCE
    else:
        return REST_INSTANCE


@pytest.fixture(scope='session')
def empty_builds_rest_instance():
    if PY2:
        LEGACY_REST_INSTANCE['build_configuration'] = 'SampleProject_Empty_Builds'
        return LEGACY_REST_INSTANCE
    else:
        REST_INSTANCE['projects'] = {'include': [{'SampleProject': {'include': ['SampleProject_Empty_Builds']}}]}
        return REST_INSTANCE


@pytest.fixture(scope='session')
def openmetrics_instance():
    return OPENMETRICS_INSTANCE


@pytest.fixture(scope="session")
def teamcity_rest_check():
    return lambda instance: TeamCityRest('teamcity', {}, [instance])


@pytest.fixture(scope="session")
def teamcity_om_check():
    return lambda instance: TeamCityOpenMetrics('teamcity', {}, [instance])
