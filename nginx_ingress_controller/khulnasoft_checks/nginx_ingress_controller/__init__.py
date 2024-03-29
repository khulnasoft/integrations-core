# (C) Khulnasoft, Inc. 2018-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from .__about__ import __version__
from .nginx_ingress_controller import NginxIngressControllerCheck

__all__ = ['__version__', 'NginxIngressControllerCheck']
