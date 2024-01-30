# (C) Khulnasoft, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>


def shared_fetch_intermediate_certs():
    return False


def instance_days_critical():
    return 7.0


def instance_days_warning():
    return 14.0


def instance_disable_generic_tags():
    return False


def instance_empty_default_hostname():
    return False


def instance_fetch_intermediate_certs():
    return False


def instance_intermediate_cert_refresh_interval():
    return 60


def instance_min_collection_interval():
    return 15


def instance_port():
    return 443


def instance_send_cert_duration():
    return False


def instance_timeout():
    return 10


def instance_tls_validate_hostname():
    return True


def instance_tls_verify():
    return True


def instance_transport():
    return 'TCP'
