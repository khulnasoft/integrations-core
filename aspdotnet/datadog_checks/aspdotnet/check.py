# (C) Khulnasoft, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from khulnasoft_checks.base.checks.windows.perf_counters.base import PerfCountersBaseCheckWithLegacySupport

from .metrics import METRICS_CONFIG


class AspdotnetCheckV2(PerfCountersBaseCheckWithLegacySupport):
    __NAMESPACE__ = 'aspdotnet'

    def get_default_config(self):
        return {'metrics': METRICS_CONFIG}
