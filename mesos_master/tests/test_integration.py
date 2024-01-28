# (C) Datadog, Inc. 2019-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import pytest

from khulnasoft_checks.base import AgentCheck
from khulnasoft_checks.base.errors import CheckException
from khulnasoft_checks.mesos_master import MesosMaster

from .common import MESOS_MASTER_VERSION, not_windows_ci

pytestmark = not_windows_ci


@pytest.mark.integration
@pytest.mark.usefixtures("dd_environment")
def test_service_check(bad_instance, aggregator):
    check = MesosMaster('mesos_master', {}, [bad_instance])

    with pytest.raises(CheckException):
        check.check(bad_instance)

    aggregator.assert_service_check('mesos_master.can_connect', count=1, status=AgentCheck.CRITICAL)


@pytest.mark.usefixtures("dd_environment")
def test_metadata(instance, khulnasoft_agent):
    check = MesosMaster('mesos_master', {}, [instance])
    check.check_id = 'test:123'

    check.check(instance)

    raw_version = MESOS_MASTER_VERSION.split('-')[0]
    major, minor, patch = raw_version.split('.')
    version_metadata = {
        'version.scheme': 'semver',
        'version.major': major,
        'version.minor': minor,
        'version.patch': patch,
        'version.raw': raw_version,
    }

    khulnasoft_agent.assert_metadata('test:123', version_metadata)
    khulnasoft_agent.assert_metadata_count(len(version_metadata))
