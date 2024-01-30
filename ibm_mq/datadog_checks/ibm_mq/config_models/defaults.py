# (C) Khulnasoft, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>


def shared_queue_manager_process_limit():
    return 1


def instance_auto_discover_channels():
    return True


def instance_auto_discover_queues():
    return False


def instance_collect_reset_queue_metrics():
    return True


def instance_collect_statistics_metrics():
    return False


def instance_convert_endianness():
    return False


def instance_disable_generic_tags():
    return False


def instance_empty_default_hostname():
    return False


def instance_host():
    return 'localhost'


def instance_min_collection_interval():
    return 15


def instance_mqcd_version():
    return 6


def instance_override_hostname():
    return False


def instance_port():
    return 1414


def instance_queue_manager_timezone():
    return 'Etc/UTC'


def instance_ssl_auth():
    return False


def instance_ssl_key_repository_location():
    return '/var/mqm/ssl-db/client/KeyringClient'


def instance_timeout():
    return 5


def instance_try_basic_auth():
    return True
