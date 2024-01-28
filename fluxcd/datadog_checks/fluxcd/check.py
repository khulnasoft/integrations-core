# (C) Datadog, Inc. 2024-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from khulnasoft_checks.base import OpenMetricsBaseCheckV2
from khulnasoft_checks.fluxcd.config_models import ConfigMixin
from khulnasoft_checks.fluxcd.metrics import METRIC_MAP


class FluxcdCheck(OpenMetricsBaseCheckV2, ConfigMixin):
    __NAMESPACE__ = "fluxcd"
    DEFAULT_METRIC_LIMIT = 0

    def get_default_config(self):
        return {"metrics": [METRIC_MAP]}
