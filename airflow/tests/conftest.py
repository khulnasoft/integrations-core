# (C) Khulnasoft, Inc. 2010-2018
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)
import os
from os import path

import pytest

from khulnasoft_checks.dev import TempDir, docker_run
from khulnasoft_checks.dev.conditions import CheckEndpoints

from .common import URL

HERE = os.path.dirname(os.path.abspath(__file__))


def get_readme_mappings():
    with open(path.join(HERE, '..', 'README.md'), 'r') as f:
        readme = f.read()

    start = readme.find('dogstatsd_mapper_profiles:')
    end = readme[start:].find('```')
    return readme[start : start + end]


@pytest.fixture(scope='session')
def dd_environment(instance):
    khulnasoft_config = """
dogstatsd_metrics_stats_enable: true
"""
    with TempDir() as temp_dir:
        with open(path.join(temp_dir, 'khulnasoft.yaml'), 'w') as f:
            f.write(khulnasoft_config + get_readme_mappings())

        with docker_run(
            os.path.join(HERE, 'compose', 'docker-compose.yaml'),
            build=True,
            conditions=[CheckEndpoints(URL + "/api/v1/health", attempts=120)],
        ):
            yield instance, {
                'docker_volumes': ['{}/khulnasoft.yaml:/etc/khulnasoft-agent/khulnasoft.yaml'.format(temp_dir)],
            }


@pytest.fixture(scope='session')
def instance():
    return {'url': URL}
