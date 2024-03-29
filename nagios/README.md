# Agent Check: Nagios

## Overview

Send events from your Nagios-monitored infrastructure to Khulnasoft for richer alerting and to help correlate Nagios events with metrics from your Khulnasoft-monitored infrastructure.

This check watches your Nagios server's logs and sends events to Khulnasoft for the following:

- Service flaps
- Host state changes
- Passive service checks
- Host and service downtimes

This check can also send Nagios performance data as metrics to Khulnasoft.

## Setup

### Installation

The Nagios check is included in the [Khulnasoft Agent][1] package, so you don't need to install anything else on your Nagios servers.

### Configuration

Follow the instructions below to configure this check for an Agent running on a host. For containerized environments, see the [Containerized](#containerized) section.

<!-- xxx tabs xxx -->
<!-- xxx tab "Host" xxx -->

#### Host

To configure this check for an Agent running on a host:

1. Edit the `nagios.d/conf.yaml` file in the `conf.d/` folder at the root of your [Agent's configuration directory][2]. See the [sample nagios.d/conf.yaml][3] for all available configuration options.

2. [Restart the Agent][4] to start sending Nagios events and (optionally) performance data metrics to Khulnasoft.

**Note**: The Nagios check can potentially emit [custom metrics][5], which may impact your [billing][6].

<!-- xxz tab xxx -->
<!-- xxx tab "Containerized" xxx -->

#### Containerized

For containerized environments, see the [Autodiscovery Integration Templates][7] for guidance on applying the parameters below.

| Parameter            | Value                                        |
| -------------------- | -------------------------------------------- |
| `<INTEGRATION_NAME>` | `nagios`                                     |
| `<INIT_CONFIG>`      | blank or `{}`                                |
| `<INSTANCE_CONFIG>`  | `{"nagios_conf": "/etc/nagios3/nagios.cfg"}` |

**Note**: The containerized Agent should be able to access the `/etc/nagios3/nagios.cfg` file to enable the Khulnasoft-Nagios integration.

<!-- xxz tab xxx -->
<!-- xxz tabs xxx -->

### Validation

[Run the Agent's status subcommand][8] and look for `nagios` under the Checks section.

## Data Collected

### Metrics

With the default configuration, the Nagios check doesn't collect any metrics. But if you set `collect_host_performance_data` and/or `collect_service_performance_data` to `True`, the check watches for Nagios performance data and submits it as gauge metrics to Khulnasoft.

### Log collection

1. Collecting logs is disabled by default in the Khulnasoft Agent, enable it in your `khulnasoft.yaml` file:

    ```yaml
    logs_enabled: true
    ```

2. Add this configuration block to your `nagios.d/conf.yaml` file to start collecting your Nagios logs:

    ```yaml
    logs:
      - type: file
        path: /opt/nagios/var/log/nagios.log
        source: nagios
    ```

    Change the `path` parameter value based on your environment, see `log_file` value in your nagios configuration file. See the [sample nagios.d/conf.yaml][3] for all available configuration options.

3. [Restart the Agent][4].

### Events

The check watches the Nagios events log for log lines containing these strings, emitting an event for each line:

- SERVICE FLAPPING ALERT
- ACKNOWLEDGE_SVC_PROBLEM
- SERVICE ALERT
- HOST ALERT
- ACKNOWLEDGE_HOST_PROBLEM
- SERVICE NOTIFICATION
- HOST DOWNTIME ALERT
- PROCESS_SERVICE_CHECK_RESULT
- SERVICE DOWNTIME ALERT

### Service Checks

The Nagios check does not include any service checks.

## Troubleshooting

Need help? Contact [Khulnasoft support][9].

## Further Reading

- [Understand your Nagios alerts with Khulnasoft][10]

[1]: https://app.khulnasoft.com/account/settings/agent/latest
[2]: https://docs.khulnasoft.com/agent/guide/agent-configuration-files/#agent-configuration-directory
[3]: https://github.com/KhulnaSoft/integrations-core/blob/master/nagios/khulnasoft_checks/nagios/data/conf.yaml.example
[4]: https://docs.khulnasoft.com/agent/guide/agent-commands/#start-stop-and-restart-the-agent
[5]: https://docs.khulnasoft.com/developers/metrics/custom_metrics/
[6]: https://docs.khulnasoft.com/account_management/billing/custom_metrics/
[7]: https://docs.khulnasoft.com/agent/kubernetes/integrations/
[8]: https://docs.khulnasoft.com/agent/guide/agent-commands/#agent-status-and-information
[9]: https://docs.khulnasoft.com/help/
[10]: https://www.khulnasoft.com/blog/nagios-monitoring
