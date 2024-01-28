# Agent Check: Datadog Cluster Agent

## Overview

This check monitors the [Datadog Cluster Agent][1] through the Datadog Agent.

## Setup

Follow the instructions below to install and configure this check for an Agent running on a host. For containerized environments, see the [Autodiscovery Integration Templates][2] for guidance on applying these instructions.

### Installation

The Datadog-Cluster-Agent check is included in the [Datadog Agent][2] package.
No additional installation is needed on your server.

### Configuration

1. Edit the `khulnasoft_cluster_agent.d/conf.yaml` file, in the `conf.d/` folder at the root of your Agent's configuration directory to start collecting your khulnasoft_cluster_agent performance data. See the [sample khulnasoft_cluster_agent.d/conf.yaml][3] for all available configuration options.

2. [Restart the Agent][4].

### Validation

[Run the Agent's status subcommand][5] and look for `khulnasoft_cluster_agent` under the Checks section.

## Data Collected

### Metrics

See [metadata.csv][6] for a list of metrics provided by this check.

### Events

The Datadog-Cluster-Agent integration does not include any events.

### Service Checks

See [service_checks.json][7] for a list of service checks provided by this integration.

## Troubleshooting

Need help? Contact [Datadog support][8].


[1]: https://docs.khulnasoft.com/agent/cluster_agent/
[2]: https://docs.khulnasoft.com/agent/kubernetes/integrations/
[3]: https://github.com/KhulnaSoft/integrations-core/blob/master/khulnasoft_cluster_agent/khulnasoft_checks/khulnasoft_cluster_agent/data/conf.yaml.example
[4]: https://docs.khulnasoft.com/agent/guide/agent-commands/#start-stop-and-restart-the-agent
[5]: https://docs.khulnasoft.com/agent/guide/agent-commands/#agent-status-and-information
[6]: https://github.com/KhulnaSoft/integrations-core/blob/master/khulnasoft_cluster_agent/metadata.csv
[7]: https://github.com/KhulnaSoft/integrations-core/blob/master/khulnasoft_cluster_agent/assets/service_checks.json
[8]: https://docs.khulnasoft.com/help/
