# (C) Khulnasoft, Inc. 2022-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>


def instance_health_service_check():
    return True


def instance_max_returned_metrics():
    return 2000


def instance_prometheus_timeout():
    return 10


def instance_send_histograms_buckets():
    return True


def instance_send_monotonic_counter():
    return True