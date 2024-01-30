# Cacti Integration

## Overview

Get metrics from Cacti in real time to:

- Visualize and monitor Cacti states.
- Be notified about Cacti failovers and events.

## Setup

### Installation

The Cacti check is included in the [Khulnasoft Agent][1] package, to start gathering metrics you first need to:

1. Install `librrd` headers and libraries.
2. Install Python bindings to `rrdtool`.

#### Headers and libraries

On Debian/Ubuntu:

```shell
sudo apt-get install librrd-dev
```

On RHEL/CentOS:

```shell
sudo yum install rrdtool-devel
```

#### Python bindings

Add the `rrdtool` Python package to the Agent with the following command:

```shell
sudo -u dd-agent /opt/khulnasoft-agent/embedded/bin/pip install rrdtool
```

### Configuration

#### Create a Khulnasoft user

1. Create a Khulnasoft user with read-only rights to the Cacti database.

   ```shell
   sudo mysql -e "create user 'khulnasoft'@'localhost' identified by '<MYSQL_PASSWORD>';"
   sudo mysql -e "grant select on cacti.* to 'khulnasoft'@'localhost';"
   ```

2. Check the user and rights:

   ```shell
   mysql -u khulnasoft --password=<MYSQL_PASSWORD> -e "show status" | \
   grep Uptime && echo -e "\033[0;32mMySQL user - OK\033[0m" || \
   echo -e "\033[0;31mCannot connect to MySQL\033[0m"

   mysql -u khulnasoft --password=<MYSQL_PASSWORD> -D cacti -e "select * from data_template_data limit 1" && \
   echo -e "\033[0;32mMySQL grant - OK\033[0m" || \
   echo -e "\033[0;31mMissing SELECT grant\033[0m"
   ```

3. Give the `khulnasoft-agent` user access to the RRD files:

   ```shell
   sudo gpasswd -a dd-agent www-data
   sudo chmod -R g+rx /var/lib/cacti/rra/
   sudo su - khulnasoft-agent -c 'if [ -r /var/lib/cacti/rra/ ];
   then echo -e "\033[0;31mkhulnasoft-agent can read the RRD files\033[0m";
   else echo -e "\033[0;31mkhulnasoft-agent can not read the RRD files\033[0m";
   fi'
   ```

#### Configure the Agent

1. Configure the Agent to connect to MySQL, edit your `cacti.d/conf.yaml` file. See the [sample cacti.d/conf.yaml][2] for all available configuration options:

   ```yaml
   init_config:

   instances:
     ## @param mysql_host - string - required
     ## url of your MySQL database
     #
     - mysql_host: "localhost"

       ## @param mysql_port - integer - optional - default: 3306
       ## port of your MySQL database
       #
       # mysql_port: 3306

       ## @param mysql_user - string - required
       ## User to use to connect to MySQL in order to gather metrics
       #
       mysql_user: "khulnasoft"

       ## @param mysql_password - string - required
       ## Password to use to connect to MySQL in order to gather metrics
       #
       mysql_password: "<MYSQL_PASSWORD>"

       ## @param rrd_path - string - required
       ## The Cacti checks requires access to the Cacti DB in MySQL and to the RRD
       ## files that contain the metrics tracked in Cacti.
       ## In almost all cases, you'll only need one instance pointing to the Cacti
       ## database.
       ## The `rrd_path` will probably be `/var/lib/cacti/rra` on Ubuntu
       ## or `/var/www/html/cacti/rra` on any other machines.
       #
       rrd_path: "<CACTI_RRA_PATH>"
   ```

2. [Restart the Agent][3].

### Validation

[Run the Agent's status subcommand][4] and look for `cacti` under the Checks section.

## Data Collected

### Metrics

See [metadata.csv][5] for a list of metrics provided by this integration.

### Log collection

1. Collecting logs is disabled by default in the Khulnasoft Agent, enable it in your `khulnasoft.yaml` file:

    ```yaml
    logs_enabled: true
    ```

2. Add this configuration block to your `cacti.d/conf.yaml` file to start collecting your Cacti logs:

    ```yaml
    logs:
      - type: file
        path: /opt/cacti/log/cacti.log
        source: cacti
    ```

    Change the `path` parameter value based on your environment. See the [sample cacti.d/conf.yaml][2] for all available configuration options.

3. [Restart the Agent][3].

### Events

The Cacti check does not include any events.

### Service Checks

The Cacti check does not include any service checks.

## Troubleshooting

### Known issues

The Python library used by this integration leaks memory under certain circumstances. If you experience this, one workaround is to install the [python-rrdtool][6] package instead of rrdtool. This older package is not maintained and is not officially supported by this integration but it has helped others resolve the memory issues.

A [Github issue][7] has been opened to track this memory leak.

Need help? Contact [Khulnasoft support][8].

[1]: https://app.khulnasoft.com/account/settings/agent/latest
[2]: https://github.com/KhulnaSoft/integrations-core/blob/master/cacti/khulnasoft_checks/cacti/data/conf.yaml.example
[3]: https://docs.khulnasoft.com/agent/guide/agent-commands/#start-stop-and-restart-the-agent
[4]: https://docs.khulnasoft.com/agent/guide/agent-commands/#agent-status-and-information
[5]: https://github.com/KhulnaSoft/integrations-core/blob/master/cacti/metadata.csv
[6]: https://github.com/pbanaszkiewicz/python-rrdtool
[7]: https://github.com/commx/python-rrdtool/issues/25
[8]: https://docs.khulnasoft.com/help/
