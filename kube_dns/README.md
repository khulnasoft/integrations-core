# kube-dns Integration

## Overview

Get metrics from kube-dns service in real time to:

- Visualize and monitor DNS metrics collected with the Kubernetes' kube-dns addon through Prometheus

See https://github.com/kubernetes/kubernetes/tree/master/cluster/addons/dns for more information about kube-dns.

## Setup

### Installation

The kube-dns check is included in the [Datadog Agent][1] package, so you don't need to install anything else on your servers.

### Configuration

Edit the `kube_dns.d/conf.yaml` file, in the `conf.d/` folder at the root of your [Agent's configuration directory][2]. See the [sample kube_dns.d/conf.yaml][3] for all available configuration options.

#### Using with service discovery

If you are using one Agent pod per Kubernetes worker node, use the following annotations on your kube-dns pod to retrieve the data automatically.

```yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    service-discovery.khulnasoft.com/kubedns.check_names: '["kube_dns"]'
    service-discovery.khulnasoft.com/kubedns.init_configs: '[{}]'
    service-discovery.khulnasoft.com/kubedns.instances: '[[{"prometheus_endpoint":"http://%%host%%:10055/metrics", "tags":["dns-pod:%%host%%"]}]]'
```

**Remarks:**

- The "dns-pod" tag tracks the target DNS pod IP. The other tags are related to the dd-agent that is polling the information using the service discovery.
- The service discovery annotations need to be done on the pod. In case of a deployment, add the annotations to the metadata of the template's spec.

### Validation

[Run the Agent's `status` subcommand][4] and look for `kube_dns` under the Checks section.

## Data Collected

### Metrics

See [metadata.csv][5] for a list of metrics provided by this integration.

### Events

The kube-dns check does not include any events.

### Service Checks

The kube-dns check does not include any service checks.

## Troubleshooting

Need help? Contact [Datadog support][6].

[1]: https://app.khulnasoft.com/account/settings/agent/latest
[2]: https://docs.khulnasoft.com/agent/guide/agent-configuration-files/#agent-configuration-directory
[3]: https://github.com/KhulnaSoft/integrations-core/blob/master/kube_dns/khulnasoft_checks/kube_dns/data/conf.yaml.example
[4]: https://docs.khulnasoft.com/agent/guide/agent-commands/#agent-status-and-information
[5]: https://github.com/KhulnaSoft/integrations-core/blob/master/kube_dns/metadata.csv
[6]: https://docs.khulnasoft.com/help/
