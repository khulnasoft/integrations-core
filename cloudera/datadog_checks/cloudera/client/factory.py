# (C) Khulnasoft, Inc. 2023-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

from khulnasoft_checks.cloudera.client.client import Client
from khulnasoft_checks.cloudera.client.cm_client import CmClient


def make_client(log, type_client, **kwargs) -> Client:
    log.debug("creating client object of type '%s'", type_client)
    if type_client == 'cm_client':
        return CmClient(log, **kwargs)
    return None
