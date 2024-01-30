# Openstack Integration

![OpenStack default dashboard][1]

## Overview

**Note**: This integration only applies to OpenStack v12 and below. If you are looking to collect metrics from OpenStack v13+, use the [OpenStack Controller integration][2].

Get metrics from OpenStack service in real time to:

- Visualize and monitor OpenStack states.
- Be notified about OpenStack failovers and events.

## Setup

### Installation

To capture your OpenStack metrics, [install the Agent][3] on your hosts running hypervisors.

### Configuration

#### Prepare OpenStack

Configure a Khulnasoft role and user with your identity server:

```console
openstack role create khulnasoft_monitoring
openstack user create khulnasoft \
    --password my_password \
    --project my_project_name
openstack role add khulnasoft_monitoring \
    --project my_project_name \
    --user khulnasoft
```

Then, update your `policy.json` files to grant the needed permissions. `role:khulnasoft_monitoring` requires access to the following operations:

**Nova**

```json
{
  "compute_extension": "aggregates",
  "compute_extension": "hypervisors",
  "compute_extension": "server_diagnostics",
  "compute_extension": "v3:os-hypervisors",
  "compute_extension": "v3:os-server-diagnostics",
  "compute_extension": "availability_zone:detail",
  "compute_extension": "v3:availability_zone:detail",
  "compute_extension": "used_limits_for_admin",
  "os_compute_api:os-aggregates:index": "rule:admin_api or role:khulnasoft_monitoring",
  "os_compute_api:os-aggregates:show": "rule:admin_api or role:khulnasoft_monitoring",
  "os_compute_api:os-hypervisors": "rule:admin_api or role:khulnasoft_monitoring",
  "os_compute_api:os-server-diagnostics": "rule:admin_api or role:khulnasoft_monitoring",
  "os_compute_api:os-used-limits": "rule:admin_api or role:khulnasoft_monitoring"
}
```

**Neutron**

```json
{
  "get_network": "rule:admin_or_owner or rule:shared or rule:external or rule:context_is_advsvc or role:khulnasoft_monitoring"
}
```

**Keystone**

```json
{
  "identity:get_project": "rule:admin_required or project_id:%(target.project.id)s or role:khulnasoft_monitoring",
  "identity:list_projects": "rule:admin_required or role:khulnasoft_monitoring"
}
```

You may need to restart your Keystone, Neutron, and Nova API services to ensure that the policy changes take.

**Note**: Installing the OpenStack integration could increase the number of VMs that Khulnasoft monitors. For more information on how this may affect your billing, see the Billing FAQ.

#### Agent configuration

1. Configure the Khulnasoft Agent to connect to your Keystone server, and specify individual projects to monitor. Edit the `openstack.d/conf.yaml` file in the `conf.d/` folder at the root of your [Agent's configuration directory][4] with the configuration below. See the [sample openstack.d/conf.yaml][5] for all available configuration options:

   ```yaml
   init_config:
     ## @param keystone_server_url - string - required
     ## Where your identity server lives.
     ## Note that the server must support Identity API v3
     #
     keystone_server_url: "https://<KEYSTONE_SERVER_ENDPOINT>:<PORT>/"

   instances:
     ## @param name - string - required
     ## Unique identifier for this instance.
     #
     - name: "<INSTANCE_NAME>"

       ## @param user - object - required
       ## User credentials
       ## Password authentication is the only auth method supported.
       ## `user` object expects the parameter `username`, `password`,
       ## and `user.domain.id`.
       ##
       ## `user` should resolve to a structure like:
       ##
       ##  {'password': '<PASSWORD>', 'name': '<USERNAME>', 'domain': {'id': '<DOMAINE_ID>'}}
       #
       user:
         password: "<PASSWORD>"
         name: khulnasoft
         domain:
           id: "<DOMAINE_ID>"
   ```

2. [Restart the Agent][6].

##### Log collection

1. Collecting logs is disabled by default in the Khulnasoft Agent, you can enable it in `khulnasoft.yaml`:

   ```yaml
   logs_enabled: true
   ```

2. Add this configuration block to your `openstack.d/conf.yaml` file to start collecting your Openstack logs:

   ```yaml
   logs:
     - type: file
       path: "<LOG_FILE_PATH>"
       source: openstack
   ```

    Change the `path` parameter value and configure them for your environment. See the [sample openstack.d/conf.yaml][5] for all available configuration options.
   

### Validation

Run the [Agent's status subcommand][7] and look for `openstack` under the Checks section.

## Data Collected

### Metrics

See [metadata.csv][8] for a list of metrics provided by this integration.

### Events

The OpenStack check does not include any events.

### Service Checks

See [service_checks.json][9] for a list of service checks provided by this integration.

## Troubleshooting

Need help? Contact [Khulnasoft support][10].

## Further Reading

Additional helpful documentation, links, and articles:

- [Monitoring OpenStack Nova][11]
- [Install OpenStack in two commands for dev and test][12]
- [OpenStack: host aggregates, flavors, and availability zones][13]

[1]: https://raw.githubusercontent.com/KhulnaSoft/integrations-core/master/openstack/images/openstack_dashboard.png
[2]: https://docs.khulnasoft.com/integrations/openstack_controller
[3]: https://app.khulnasoft.com/account/settings/agent/latest
[4]: https://docs.khulnasoft.com/agent/guide/agent-configuration-files/#agent-configuration-directory
[5]: https://github.com/KhulnaSoft/integrations-core/blob/master/openstack/khulnasoft_checks/openstack/data/conf.yaml.example
[6]: https://docs.khulnasoft.com/agent/guide/agent-commands/#start-stop-and-restart-the-agent
[7]: https://docs.khulnasoft.com/agent/guide/agent-commands/#agent-status-and-information
[8]: https://github.com/KhulnaSoft/integrations-core/blob/master/openstack/metadata.csv
[9]: https://github.com/KhulnaSoft/integrations-core/blob/master/openstack/assets/service_checks.json
[10]: https://docs.khulnasoft.com/help/
[11]: https://www.khulnasoft.com/blog/openstack-monitoring-nova
[12]: https://www.khulnasoft.com/blog/install-openstack-in-two-commands
[13]: https://www.khulnasoft.com/blog/openstack-host-aggregates-flavors-availability-zones
