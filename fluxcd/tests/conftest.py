# (C) Khulnasoft, Inc. 2024-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os
from unittest import mock

import pytest

from khulnasoft_checks.dev import get_here
from khulnasoft_checks.dev.kind import kind_run
from khulnasoft_checks.dev.kube_port_forward import port_forward
from khulnasoft_checks.dev.subprocess import run_command
from khulnasoft_checks.fluxcd import FluxcdCheck

HERE = get_here()
opj = os.path.join


def setup_fluxcd():
    run_command(["kubectl", "apply", "--filename", opj(HERE, 'kind', "install.yaml")])
    run_command(
        [
            "kubectl",
            "wait",
            "deployments",
            "--all",
            "--for=condition=Available",
            "--namespace",
            "flux-system",
            "--timeout=300s",
        ]
    )


@pytest.fixture(scope='session')
def dd_environment():
    with kind_run(conditions=[setup_fluxcd]) as kubeconfig:
        with port_forward(kubeconfig, 'flux-system', 8080, 'deployment', 'source-controller') as (
            src_controller_host,
            src_controller_port,
        ):
            src_controller_endpoint = 'http://{}:{}/metrics'.format(src_controller_host, src_controller_port)

            instance = {
                'openmetrics_endpoint': src_controller_endpoint,
            }
            yield instance


@pytest.fixture
def instance():
    return {
        "openmetrics_endpoint": "http://localhost:3000/metrics",
    }


@pytest.fixture
def check(instance):
    return FluxcdCheck("fluxcd", {}, [instance])


@pytest.fixture()
def mock_metrics_v1():
    fixture_file = os.path.join(os.path.dirname(__file__), "fixtures", "metrics-v1.txt")

    with open(fixture_file, "r") as f:
        content = f.read()

    with mock.patch(
        "requests.get",
        return_value=mock.MagicMock(
            status_code=200,
            iter_lines=lambda **kwargs: content.split("\n"),
            headers={"Content-Type": "text/plain"},
        ),
    ):
        yield


@pytest.fixture()
def mock_metrics_v2():
    fixture_file = os.path.join(os.path.dirname(__file__), "fixtures", "metrics-v2.txt")

    with open(fixture_file, "r") as f:
        content = f.read()

    with mock.patch(
        "requests.get",
        return_value=mock.MagicMock(
            status_code=200,
            iter_lines=lambda **kwargs: content.split("\n"),
            headers={"Content-Type": "text/plain"},
        ),
    ):
        yield
