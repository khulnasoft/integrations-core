# Agent Check: Twistlock

## Overview

[Prisma Cloud Compute Edition][1] is a security scanner. It scans containers, hosts, and packages to find vulnerabilities and compliance issues.

## Setup

### Installation

The Prisma Cloud Compute Edition check is included in the [Khulnasoft Agent][2] package, so you do not need to install anything else on your server.

### Configuration

<!-- xxx tabs xxx -->
<!-- xxx tab "Host" xxx -->

#### Host

To configure this check for an Agent running on a host:

##### Metric collection

1. Edit the `twistlock.d/conf.yaml` file, in the `conf.d/` folder at the root of your Agent's configuration directory to start collecting your twistlock performance data. See the [sample twistlock.d/conf.yaml][3] for all available configuration options.

2. [Restart the Agent][4].

<!-- xxz tab xxx -->
<!-- xxx tab "Containerized" xxx -->

#### Containerized

For containerized environments, see the [Autodiscovery Integration Templates][5] for guidance on applying the parameters below.

##### Metric collection

| Parameter            | Value                                                                               |
| -------------------- | ----------------------------------------------------------------------------------- |
| `<INTEGRATION_NAME>` | `twistlock`                                                                         |
| `<INIT_CONFIG>`      | blank or `{}`                                                                       |
| `<INSTANCE_CONFIG>`  | `{"url":"http://%%host%%:8083", "username":"<USERNAME>", "password": "<PASSWORD>"}` |

###### Kubernetes

If you're using Kubernetes, add the config to replication controller section of twistlock_console.yaml before deploying:

```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: twistlock-console
  namespace: twistlock
spec:
  replicas: 1
  selector:
    name: twistlock-console
  template:
    metadata:
      annotations:
        ad.khulnasoft.com/twistlock-console.check_names: '["twistlock"]'
        ad.khulnasoft.com/twistlock-console.init_configs: "[{}]"
        ad.khulnasoft.com/twistlock-console.instances: '[{"url":"http://%%host%%:8083", "username":"<USERNAME>", "password": "<PASSWORD>"}]'
        ad.khulnasoft.com/twistlock-console.logs: '[{"source": "twistlock", "service": "twistlock"}]'
      name: twistlock-console
      namespace: twistlock
      labels:
        name: twistlock-console
```

##### Log collection

<!-- partial
{{< site-region region="us3" >}}
**Log collection is not supported for the Khulnasoft {{< region-param key="dd_site_name" >}} site**.
{{< /site-region >}}
partial -->

_Available for Agent versions >6.0_

Collecting logs is disabled by default in the Khulnasoft Agent. To enable it, see [Kubernetes Log Collection][6].

| Parameter      | Value                                             |
| -------------- | ------------------------------------------------- |
| `<LOG_CONFIG>` | `{"source": "twistlock", "service": "twistlock"}` |

###### Kubernetes

1. Collecting logs is disabled by default in the Khulnasoft Agent. Enable it in your [DaemonSet configuration][7]:

   ```yaml
     #(...)
       env:
         #(...)
         - name: DD_LOGS_ENABLED
             value: "true"
         - name: DD_LOGS_CONFIG_CONTAINER_COLLECT_ALL
             value: "true"
     #(...)
   ```

2. Mount the Docker socket to the Khulnasoft Agent. See the Khulnasoft Kubernetes [example manifests][8].

3. Make sure the log section is included in the Pod annotation for the defender, where the container name can be found just below in the pod spec:

   ```yaml
   ad.khulnasoft.com/<container-name>.logs: '[{"source": "twistlock", "service": "twistlock"}]'
   ```

4. [Restart the Agent][4].

###### Docker

1. Collecting logs is disabled by default in the Khulnasoft Agent. Enable it with the environment variable:

   ```shell
   DD_LOGS_ENABLED=true
   ```

2. Add a label on the defender container:

   ```yaml
   ad.khulnasoft.com/<container-name>.logs: '[{"source": "twistlock", "service": "twistlock"}]'
   ```

3. Mount the Docker socket to the Khulnasoft Agent. More information about the required configuration to collect logs with the Khulnasoft Agent available in [Docker Log Collection][9].

4. [Restart the Agent][4].

<!-- xxz tab xxx -->
<!-- xxz tabs xxx -->

### Validation

Run the [Agent's status subcommand][10] and look for `twistlock` under the Checks section.

## Data Collected

### Metrics

See [metadata.csv][11] for a list of metrics provided by this check.

### Events

Prisma Cloud Compute Edition sends an event when a new CVE is found.

### Service Checks

See [service_checks.json][12] for a list of service checks provided by this integration.

## Troubleshooting

Need help? Contact [Khulnasoft support][13].


[1]: https://www.paloaltonetworks.com/prisma/cloud
[2]: https://app.khulnasoft.com/account/settings/agent/latest
[3]: https://github.com/KhulnaSoft/integrations-core/blob/master/twistlock/khulnasoft_checks/twistlock/data/conf.yaml.example
[4]: https://docs.khulnasoft.com/agent/guide/agent-commands/#start-stop-and-restart-the-agent
[5]: https://docs.khulnasoft.com/agent/kubernetes/integrations/
[6]: https://docs.khulnasoft.com/agent/kubernetes/log/?tab=containerinstallation#setup
[7]: https://docs.khulnasoft.com/agent/kubernetes/daemonset_setup/#log-collection
[8]: https://docs.khulnasoft.com/agent/kubernetes/?tab=daemonset
[9]: https://docs.khulnasoft.com/agent/docker/log/?tab=containerinstallation
[10]: https://docs.khulnasoft.com/agent/guide/agent-commands/#agent-status-and-information
[11]: https://github.com/KhulnaSoft/integrations-core/blob/master/twistlock/metadata.csv
[12]: https://github.com/KhulnaSoft/integrations-core/blob/master/twistlock/assets/service_checks.json
[13]: https://docs.khulnasoft.com/help/
