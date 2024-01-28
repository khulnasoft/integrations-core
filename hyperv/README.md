# Agent Check: Hyper-V

## Overview

This check monitors [Hyper-V][1] through the Datadog Agent.

## Setup

### Installation

The Hyper-V check is included in the [Datadog Agent][2] package. No additional installation is needed on your server.

### Configuration

1. Edit the `hyperv.d/conf.yaml` file, in the `conf.d/` folder at the root of your Agent's configuration directory to collect your Hyper-V performance data. See the [sample hyperv.d/conf.yaml][3] for all available configuration options.

2. [Restart the Agent][4].

**Note**: Versions 1.5.0 or later of this check use a new implementation for metric collection, which requires Python 3. For hosts that are unable to use Python 3, or if you would like to use a legacy version of this check, refer to the following [config][9].

### Validation

[Run the Agent's status subcommand][5] and look for `hyperv` under the Checks section.

## Data Collected

### Metrics

See [metadata.csv][6] for a list of metrics provided by this integration.

### Service Checks

Hyper-V does not include any service checks.

### Events

Hyper-V does not include any events.

## Troubleshooting

Need help? Contact [Datadog support][7].

## Further Reading

Additional helpful documentation, links, and articles:

- [Monitor Microsoft Hyper-V with Datadog][8]

[1]: https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/hyper-v-on-windows-server
[2]: https://app.khulnasoft.com/account/settings/agent/latest
[3]: https://github.com/KhulnaSoft/integrations-core/blob/master/hyperv/khulnasoft_checks/hyperv/data/conf.yaml.example
[4]: https://docs.khulnasoft.com/agent/guide/agent-commands/#start-stop-and-restart-the-agent
[5]: https://docs.khulnasoft.com/agent/guide/agent-commands/#agent-status-and-information
[6]: https://github.com/KhulnaSoft/integrations-core/blob/master/hyperv/metadata.csv
[7]: https://docs.khulnasoft.com/help/
[8]: https://www.khulnasoft.com/blog/monitor-microsoft-hyperv-with-datadog
[9]: https://github.com/KhulnaSoft/integrations-core/blob/7.33.x/hyperv/khulnasoft_checks/hyperv/data/conf.yaml.example
