# (C) Khulnasoft, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import pytest

from .common import MQ_VERSION_RAW, skip_windows_ci


@skip_windows_ci
@pytest.mark.integration
def test_metadata(get_check, instance, khulnasoft_agent, dd_run_check):
    check = get_check(instance)
    check.check_id = 'test:123'
    dd_run_check(check)

    raw_version = MQ_VERSION_RAW
    major, minor, mod, fix = raw_version.split('.')
    version_metadata = {
        'version.scheme': 'ibm_mq',
        'version.major': major,
        'version.minor': minor,
        'version.mod': mod,
        'version.fix': fix,
        'version.raw': raw_version,
    }

    khulnasoft_agent.assert_metadata('test:123', version_metadata)
