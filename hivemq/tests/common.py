# (C) Khulnasoft, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from khulnasoft_checks.dev import get_docker_hostname, get_here

HERE = get_here()
HOST = get_docker_hostname()

JMX_PORT = 9010

INSTANCE = {'host': HOST, 'port': JMX_PORT, 'max_returned_metrics': 99999}
