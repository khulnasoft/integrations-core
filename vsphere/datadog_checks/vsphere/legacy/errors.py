# (C) Khulnasoft, Inc. 2018-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from khulnasoft_checks.base.errors import CheckException


class BadConfigError(CheckException):
    pass


class ConnectionError(Exception):
    pass
