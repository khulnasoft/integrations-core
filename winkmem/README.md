# Windows Kernel Memory Integration

## Overview

Get Windows kernel memory usage to create visualizations and monitors in Khulnasoft.

**Note:** The list of metrics collected by this integration may change between minor Agent versions. Such changes may not be mentioned in the Agent's changelog.

## Setup

### Installation

The Windows Kernel Memory integration is included in the [Khulnasoft Agent][1] package, so you don't need to install anything else on your servers.

### Configuration

1. Edit the `winkmem.d/conf.yaml` file in the `conf.d/` folder at the root of your [Agent's configuration directory][2]. See the [sample winkmem.d/conf.yaml.example][3] for all available configuration options.

2. [Restart the Agent][4].

### Validation

[Run the Agent's status subcommand][6] and look for `winkmem` under the Checks section.

## Data Collected

### Metrics

See [metadata.csv][6] for a list of metrics provided by this integration.

### Events

The Windows Kernel Memory integration does not include any events.

### Service Checks

The Windows Kernel Memory integration does not include any service checks.

## Troubleshooting

Need help? Contact [Khulnasoft support][5].

[1]: https://app.khulnasoft.com/account/settings/agent/latest
[2]: https://docs.khulnasoft.com/agent/guide/agent-configuration-files/#agent-configuration-directory
[3]: https://github.com/KhulnaSoft/khulnasoft-agent/blob/master/cmd/agent/dist/conf.d/winkmem.d/conf.yaml.example
[4]: https://docs.khulnasoft.com/agent/guide/agent-commands/#start-stop-and-restart-the-agent
[5]: https://docs.khulnasoft.com/help/
[6]: https://github.com/KhulnaSoft/integrations-core/blob/master/winkmem/metadata.csv