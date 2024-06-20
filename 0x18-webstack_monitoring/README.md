# 0x18. Webstack Monitoring

## Table of Contents

- [Introduction](#introduction)
- [Background Context](#background-context)
- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [Task 0: Sign up for Datadog and install datadog-agent](#task-0-sign-up-for-datadog-and-install-datadog-agent)
  - [Task 1: Monitor some metrics](#task-1-monitor-some-metrics)
  - [Task 2: Create a dashboard](#task-2-create-a-dashboard)
- [Usage](#usage)
- [License](#license)

## Introduction {#introduction}

This project focuses on implementing webstack monitoring using Datadog. Monitoring is essential for understanding the performance and health of software systems and servers. This project will guide you through setting up monitoring for application and server metrics using Datadog.

## Background Context {#background-context}

“You cannot fix or improve what you cannot measure” is a famous saying in the tech industry. Monitoring software systems is crucial in the data-driven age to ensure they behave as expected and are not overloaded. Web stack monitoring is divided into two main categories:

- Application Monitoring: Gathering data about your running software.
- Server Monitoring: Gathering data about your server's performance metrics.

## Learning Objectives {#learning-objectives}

By the end of this project, you should be able to explain:

- Why monitoring is needed.
- The two main areas of monitoring.
- What access logs for a web server (such as Nginx) are.
- What error logs for a web server (such as Nginx) are.

## Requirements {#requirements}

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 16.04 LTS
- All files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck (version 0.3.7) without errors
- The first line of all Bash scripts should be `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what the script does

## Tasks {#tasks}

### Task 0: Sign up for Datadog and install datadog-agent

1. Sign up for a free Datadog account on the US website: Datadog US.
2. Use the US1 region.
3. Follow the instructions on the Datadog website to install the Datadog agent on web-01.
4. Create an application key.
5. Copy-paste your Datadog API key and application key into your Intranet user profile.
6. Verify that `web-01` is visible in Datadog under the hostname `XX-web-01`.

### Task 1: Monitor some metrics

1. Set up a monitor that checks the number of read requests issued to the device per second.
2. Set up a monitor that checks the number of write requests issued to the device per second.

### Task 2: Create a dashboard

1. Create a new dashboard in Datadog.
2. Add at least 4 widgets to the dashboard. The widgets can monitor any metrics you prefer.
3. Create an answer file `2-setup_datadog` with the `dashboard_id` on the first line. To get the dashboard ID, you may need to use Datadog’s API.

## Usage {#usage}

To complete the tasks, follow these steps:

1. Set up Datadog:
    - Sign up for an account on Datadog US.
    - Follow the setup instructions to install the Datadog agent on `web-01`.
    - Create an application key and enter your Datadog API key and application key in your user profile on the Intranet.

2. Monitor Metrics:
    - Use the Datadog dashboard to set up monitors for read and write requests per second.

3. Create a Dashboard:
    - Use the Datadog UI to create a new dashboard and add widgets.
    - Use the Datadog API to retrieve the `dashboard_id` and save it in the `2-setup_datadog` file.

## License {#license}

This project is licensed under the MIT License.
