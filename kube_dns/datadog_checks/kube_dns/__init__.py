# (C) Datadog, Inc. 2018-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from .__about__ import __version__
from .kube_dns import KubeDNSCheck

__all__ = ['__version__', 'KubeDNSCheck']
