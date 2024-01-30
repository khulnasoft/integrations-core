# (C) Khulnasoft, Inc. 2018-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)


class APIException(Exception):
    pass


class APIAuthException(Exception):
    pass


class APIConnectionException(APIException):
    pass


class APIParsingException(APIException):
    pass
