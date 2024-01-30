# (C) Khulnasoft, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>


def shared_access_denied_cache_duration():
    return 120


def shared_pid_cache_duration():
    return 120


def shared_shared_process_list_cache_duration():
    return 120


def instance_collect_children():
    return False


def instance_disable_generic_tags():
    return False


def instance_empty_default_hostname():
    return False


def instance_exact_match():
    return True


def instance_ignore_denied_access():
    return True


def instance_min_collection_interval():
    return 15


def instance_pid_cache_duration():
    return 120


def instance_try_sudo():
    return False
