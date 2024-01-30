# Pivotal Container Service Integration

## Overview

This integration monitors [Pivotal Container Service][1] clusters.

## Setup

Since Khulnasoft already integrates with Kubernetes, it is ready-made to monitor Pivotal Kubernetes Service (PKS). You can use the Khulnasoft [Cluster Monitoring tile][7] along with this integration to monitor your cluster.

Install the Khulnasoft Agent on each non-worker VM in your PKS environment. In environments without Pivotal Application Service (PAS) installed, select the `Resource Config` section of the tile and set `instances` of the `khulnasoft-firehose-nozzle` to `0`.

### Metric collection

Monitoring PKS requires that you set up the Khulnasoft integration for [Kubernetes][2].

### Log collection

_Available for Agent versions >6.0_

The setup is exactly the same as for Kubernetes.
To start collecting logs from all your containers, use your Khulnasoft Agent [environment variables][3].

You can also take advantage of DaemonSets to [automatically deploy the Khulnasoft Agent on all your nodes][4].

Follow the [container log collection steps][5] to learn more about those environment variables and discover more advanced setup options.

## Troubleshooting

Need help? Contact [Khulnasoft support][6].

[1]: https://pivotal.io/platform/pivotal-container-service
[2]: https://docs.khulnasoft.com/integrations/kubernetes/
[3]: https://docs.khulnasoft.com/agent/basic_agent_usage/kubernetes/#log-collection-setup
[4]: https://docs.khulnasoft.com/agent/basic_agent_usage/kubernetes/#container-installation
[5]: https://docs.khulnasoft.com/logs/log_collection/docker/#option-2-container-installation
[6]: https://docs.khulnasoft.com/help/
[7]: https://network.pivotal.io/products/khulnasoft
