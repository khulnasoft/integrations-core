# (C) Khulnasoft, Inc. 2019-present
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)
import os

import pytest

from khulnasoft_checks.fluentd import Fluentd

from .common import CHECK_NAME, FLUENTD_CONTAINER_NAME, FLUENTD_VERSION, HERE
from .util import requires_above_1_8, requires_below_1_8

pytestmark = [pytest.mark.usefixtures("dd_environment"), pytest.mark.integration, pytest.mark.metadata]

CHECK_ID = 'test:123'
VERSION_MOCK_SCRIPT = os.path.join(HERE, 'mock', 'fluentd_version.py')


def test_collect_metadata_instance(aggregator, khulnasoft_agent, instance, dd_run_check):
    instance['fluentd'] = 'docker exec {} fluentd'.format(FLUENTD_CONTAINER_NAME)

    check = Fluentd(CHECK_NAME, {}, [instance])
    check.check_id = CHECK_ID
    dd_run_check(check)

    major, minor, patch = FLUENTD_VERSION.split('.')
    version_metadata = {
        'version.raw': FLUENTD_VERSION,
        'version.scheme': 'semver',
        'version.major': major,
        'version.minor': minor,
        'version.patch': patch,
    }

    khulnasoft_agent.assert_metadata(CHECK_ID, version_metadata)
    khulnasoft_agent.assert_metadata_count(5)


@requires_below_1_8
def test_collect_metadata_missing_version(aggregator, khulnasoft_agent, dd_run_check, instance):
    instance["fluentd"] = "python {} 'fluentd not.a.version'".format(VERSION_MOCK_SCRIPT)

    check = Fluentd(CHECK_NAME, {}, [instance])
    check.check_id = CHECK_ID
    dd_run_check(check)

    khulnasoft_agent.assert_metadata(CHECK_ID, {})
    khulnasoft_agent.assert_metadata_count(0)


@requires_below_1_8
def test_collect_metadata_invalid_binary(khulnasoft_agent, instance):
    instance['fluentd'] = '/bin/does_not_exist'

    check = Fluentd(CHECK_NAME, {}, [instance])
    check.check_id = CHECK_ID
    check.check(None)

    khulnasoft_agent.assert_metadata(CHECK_ID, {})
    khulnasoft_agent.assert_metadata_count(0)


@requires_above_1_8
def test_collect_metadata_invalid_binary_with_endpoint(khulnasoft_agent, instance):
    instance['fluentd'] = '/bin/does_not_exist'

    check = Fluentd(CHECK_NAME, {}, [instance])
    check.check_id = CHECK_ID
    check.check(None)

    major, minor, patch = FLUENTD_VERSION.split('.')
    version_metadata = {
        'version.raw': FLUENTD_VERSION,
        'version.scheme': 'semver',
        'version.major': major,
        'version.minor': minor,
        'version.patch': patch,
    }

    khulnasoft_agent.assert_metadata(CHECK_ID, version_metadata)
    khulnasoft_agent.assert_metadata_count(5)
