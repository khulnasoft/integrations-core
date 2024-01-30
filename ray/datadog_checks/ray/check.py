# (C) Khulnasoft, Inc. 2023-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

from khulnasoft_checks.base import OpenMetricsBaseCheckV2
from khulnasoft_checks.ray.config_models import ConfigMixin

from .metrics import METRIC_MAP


class RayCheck(OpenMetricsBaseCheckV2, ConfigMixin):
    __NAMESPACE__ = 'ray'
    DEFAULT_METRIC_LIMIT = 0

    def get_default_config(self):
        return {
            "metrics": [METRIC_MAP],
        }
