# Agent Check: Presto

## Overview

This check collects [Presto][1] metrics, for example:

- Overall activity metrics: completed/failed queries, data input/output size, execution time.
- Performance metrics: cluster memory, input CPU, execution CPU time.

## Setup

Follow the instructions below to install and configure this check for an Agent running on a host. For containerized environments, see the [Autodiscovery Integration Templates][2] for guidance on applying these instructions.

### Installation

The Presto check is included in the [Khulnasoft Agent][3] package.
No additional installation is needed on your server. Install the Agent on each Coordinator and Worker node from which you wish to collect usage and performance metrics.

### Configuration

1. Edit the `presto.d/conf.yaml` file, in the `conf.d/` folder at the root of your Agent's configuration directory to start collecting your Presto performance data. See the [sample presto.d/conf.yaml][4] for all available configuration options.

    This check has a limit of 350 metrics per instance. The number of returned metrics is indicated in the info page. You can specify the metrics you are interested in by editing the configuration below. To learn how to customize the metrics to collect, see the [JMX Checks documentation][5] for more detailed instructions. If you need to monitor more metrics, contact [Khulnasoft support][6].

2. [Restart the Agent][7].

#### Metric collection

Use the default configuration of your `presto.d/conf.yaml` file to activate the collection of your Presto metrics. See the sample [presto.d/conf.yaml][4] for all available configuration options.

#### Log collection

_Available for Agent versions >6.0_

1. Collecting logs is disabled by default in the Khulnasoft Agent. Enable it in your `khulnasoft.yaml` file:

   ```yaml
   logs_enabled: true
   ```

2. Add this configuration block to your `presto.d/conf.yaml` file to start collecting your Presto logs:

   ```yaml
   logs:
     - type: file
       path: /var/log/presto/*.log
       source: presto
       service: "<SERVICE_NAME>"
   ```

    Change the `path` and `service` parameter values and configure them for your environment. See the sample [presto.d/conf.yaml][4] for all available configuration options.

3. [Restart the Agent][7].

### Validation

Run the [Agent's status subcommand][8] and look for `presto` under the Checks section.

## Data Collected

### Metrics

See [metadata.csv][9] for a list of metrics provided by this check.

### Events

Presto does not include any events.

### Service Checks

See [service_checks.json][10] for a list of service checks provided by this integration.

## Troubleshooting

Need help? Contact [Khulnasoft support][6].


[1]: https://docs.khulnasoft.com/integrations/presto/
[2]: https://docs.khulnasoft.com/agent/kubernetes/integrations/
[3]: https://app.khulnasoft.com/account/settings/agent/latest
[4]: https://github.com/KhulnaSoft/integrations-core/blob/master/presto/khulnasoft_checks/presto/data/conf.yaml.example
[5]: https://docs.khulnasoft.com/integrations/java/
[6]: https://docs.khulnasoft.com/help/
[7]: https://docs.khulnasoft.com/agent/guide/agent-commands/#start-stop-and-restart-the-agent
[8]: https://docs.khulnasoft.com/agent/guide/agent-commands/#agent-status-and-information
[9]: https://github.com/KhulnaSoft/integrations-core/blob/master/presto/metadata.csv
[10]: https://github.com/KhulnaSoft/integrations-core/blob/master/presto/assets/service_checks.json
