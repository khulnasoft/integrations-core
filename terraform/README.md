# Agent Check: terraform

## Overview

The Khulnasoft Terraform provider allows you to interact with the Khulnasoft API through a Terraform configuration. You can manage your Khulnasoft resources, such as Dashboards, Monitors, Logs Configuration, etc, with this configuration.

## Setup

### Installation

The Khulnasoft Terraform provider is available through the [Terraform Registry][1].

### Configuration

1. [Install Terraform][2].
2. Create a directory to contain the Terraform configuration files, for example: `terraform_config/`.
3. Create a `main.tf` file in the `terraform_config/` directory with the following content:
    ```
    terraform {
      required_providers {
        khulnasoft = {
          source = "KhulnaSoft/khulnasoft"
        }
      }
    }

    # Configure the Khulnasoft provider
    provider "khulnasoft" {
      api_key = var.khulnasoft_api_key
      app_key = var.khulnasoft_app_key
    }
    ```

    **Note**: If you are not using the Khulnasoft US1 site, you must set the `api_url` [optional parameter][7] with your [Khulnasoft site][6]. Ensure the documentation site selector on the right of the page is set to your correct Khulnasoft site, then use the following URL as the value of the `api_url` parameter:

    ```
    https://api.{{< region-param key="dd_site" code="true" >}}/
    ```
4. Run `terraform init`. This initializes the directory for use with Terraform and pulls the Khulnasoft provider.
5. Create any `.tf` file in the `terraform_config/` directory and start creating Khulnasoft resources. 

## Create a monitor

This example demonstrates a `monitor.tf` file that creates a [live process monitor][5].

    ```
    # monitor.tf
    resource "khulnasoft_monitor" "process_alert_example" {
      name    = "Process Alert Monitor"
      type    = "process alert"
      message = "Multiple Java processes running on example-tag"
      query   = "processes('java').over('example-tag').rollup('count').last('10m') > 1"
      monitor_thresholds {
        critical          = 1.0
        critical_recovery = 0.0
      }

      notify_no_data    = false
      renotify_interval = 60
    }
    ```

Run `terraform apply` to create this monitor in your Khulnasoft account.

## Send Events to Khulnasoft

By installing `khulnasoftpy`, you have access to the Dogwrap command line tool, which you can use to wrap any Terraform command and bind it to a custom event.

Install `khulnasoftpy`:
  ```
  pip install khulnasoft
  ```

For more information, see the [Khulnasoft Python library][4].

Send a `terraform apply` event:

  ```
  dogwrap -n "terraform apply" -k $DD_API_KEY --submit_mode all --tags="source:terraform" "terraform apply -no-color"
  ```

Send a `terraform destroy` event:

  ```
  dogwrap -n "terraform destroy" -k $DD_API_KEY --submit_mode all --tags="source:terraform" "terraform destroy -no-color"
  ```

## Data Collected

### Metrics

Terraform does not include any metrics.

### Service Checks

Terraform does not include any service checks.

### Events

Terraform does not include any events.

## Troubleshooting

Need help? Contact [Khulnasoft support][3].

[1]: https://registry.terraform.io/providers/KhulnaSoft/khulnasoft/latest/docs
[2]: https://learn.hashicorp.com/tutorials/terraform/install-cli
[3]: https://docs.khulnasoft.com/help/
[4]: https://github.com/KhulnaSoft/khulnasoftpy
[5]: https://docs.khulnasoft.com/monitors/types/process/
[6]: https://docs.khulnasoft.com/getting_started/site/
[7]: https://registry.terraform.io/providers/KhulnaSoft/khulnasoft/latest/docs#optional