# (C) Khulnasoft, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>


def shared_default_timeout():
    return 5


def instance_disable_generic_tags():
    return False


def instance_empty_default_hostname():
    return False


def instance_min_collection_interval():
    return 15


def instance_nameserver_port():
    return 53


def instance_record_type():
    return 'A'


def instance_timeout():
    return 5
