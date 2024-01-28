# (C) Datadog, Inc. 2022-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import click
from khulnasoft_checks.dev.tooling.commands.validate.agent_reqs import agent_reqs
from khulnasoft_checks.dev.tooling.commands.validate.agent_signature import legacy_signature
from khulnasoft_checks.dev.tooling.commands.validate.all_validations import all
from khulnasoft_checks.dev.tooling.commands.validate.codeowners import codeowners
from khulnasoft_checks.dev.tooling.commands.validate.config import config
from khulnasoft_checks.dev.tooling.commands.validate.dashboards import dashboards
from khulnasoft_checks.dev.tooling.commands.validate.dep import dep
from khulnasoft_checks.dev.tooling.commands.validate.eula import eula
from khulnasoft_checks.dev.tooling.commands.validate.imports import imports
from khulnasoft_checks.dev.tooling.commands.validate.integration_style import integration_style
from khulnasoft_checks.dev.tooling.commands.validate.jmx_metrics import jmx_metrics
from khulnasoft_checks.dev.tooling.commands.validate.license_headers import license_headers
from khulnasoft_checks.dev.tooling.commands.validate.models import models
from khulnasoft_checks.dev.tooling.commands.validate.package import package
from khulnasoft_checks.dev.tooling.commands.validate.readmes import readmes
from khulnasoft_checks.dev.tooling.commands.validate.saved_views import saved_views
from khulnasoft_checks.dev.tooling.commands.validate.service_checks import service_checks
from khulnasoft_checks.dev.tooling.commands.validate.typos import typos

from ddev.cli.validate.ci import ci
from ddev.cli.validate.http import http
from ddev.cli.validate.licenses import licenses
from ddev.cli.validate.manifest import manifest
from ddev.cli.validate.metadata import metadata
from ddev.cli.validate.openmetrics import openmetrics


@click.group(short_help='Verify certain aspects of the repo')
def validate():
    """
    Verify certain aspects of the repo.
    """


validate.add_command(agent_reqs)
validate.add_command(all)
validate.add_command(ci)
validate.add_command(codeowners)
validate.add_command(config)
validate.add_command(dashboards)
validate.add_command(dep)
validate.add_command(eula)
validate.add_command(http)
validate.add_command(imports)
validate.add_command(integration_style)
validate.add_command(jmx_metrics)
validate.add_command(legacy_signature)
validate.add_command(license_headers)
validate.add_command(licenses)
validate.add_command(manifest)
validate.add_command(metadata)
validate.add_command(models)
validate.add_command(openmetrics)
validate.add_command(package)
validate.add_command(readmes)
validate.add_command(saved_views)
validate.add_command(service_checks)
validate.add_command(typos)
