# (C) Khulnasoft, Inc. 2018-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os
import sys

import mock
import pytest

from khulnasoft_checks.dev import temp_dir
from khulnasoft_checks.http_check.utils import _get_ca_certs_paths, get_ca_certs_path


def test_get_ca_certs_path():
    with mock.patch('khulnasoft_checks.http_check.utils._get_ca_certs_paths') as gp:
        # no certs found
        gp.return_value = []
        assert get_ca_certs_path() is None
        # one cert file was found
        # let's avoid creating a real file just for the sake of mocking a cert
        # and use __file__ instead
        gp.return_value = [__file__]
        assert get_ca_certs_path() == __file__


def test__get_ca_certs_paths_ko():
    """
    When `embedded` folder is not found, it should raise OSError
    """
    with pytest.raises(OSError):
        _get_ca_certs_paths()


def test__get_ca_certs_paths(embedded_dir):
    with mock.patch('khulnasoft_checks.http_check.utils.os.path.dirname') as dirname:
        # create a tmp `embedded` folder
        with temp_dir() as tmp:
            target = os.path.join(tmp, embedded_dir)
            os.mkdir(target)
            # point `dirname()` there
            dirname.return_value = target

            # tornado not found
            paths = _get_ca_certs_paths()
            assert len(paths) == 2
            assert paths[0].startswith(target)
            assert paths[1] == '/etc/ssl/certs/ca-certificates.crt'

            # mock tornado's presence
            sys.modules['tornado'] = mock.MagicMock(__file__='.')
            paths = _get_ca_certs_paths()
            assert len(paths) == 3
            assert paths[1].endswith('ca-certificates.crt')
            assert paths[2] == '/etc/ssl/certs/ca-certificates.crt'
