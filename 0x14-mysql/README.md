# MySQL

This repository contains scripts and configurations related to setting up and managing MySQL databases on Ubuntu 16.04 servers.

## Contents

- [Task 0: Install MySQL](#task-0-install-mysql)
- [Task 1: Let us in!](#task-1-let-us-in)
- [Task 2: If only you could see what I've seen with your eyes](#task-2-if-only-you-could-see-what-ive-seen-with-your-eyes)
- [Task 3: Quite an experience to live in fear, isn't it?](#task-3-quite-an-experience-to-live-in-fear-isnt-it)
- [Task 4: Setup a Primary-Replica infrastructure using MySQL](#task-4-setup-a-primary-replica-infrastructure-using-mysql)
- [Task 5: MySQL backup](#task-5-mysql-backup)

## Description

This project covers topics such as #DevOps, #SysAdmin, and #MySQL.

## Task 0: Install MySQL

First, MySQL 5.7.x is installed on both web-01 and web-02 servers. The script `0-install_mysql.sh` accomplishes this task. Once installed, the script checks the MySQL version to ensure it meets the requirements.

## Task 1: Let us in!

This task involves creating a MySQL user named `holberton_user` on both web-01 and web-02 servers. The user has permissions to check the primary/replica status of the databases. The script `1-create_user.sh` handles this setup.

## Task 2: If only you could see what I've seen with your eyes

To set up replication, a database named `tyrell_corp` is created on the primary MySQL server (web-01). The database contains a table named `nexus6` with at least one entry. The script `2-setup_replication.sh` performs these actions.

## Task 3: Quite an experience to live in fear, isn't it?

Before setting up replication, a new user named `replica_user` is created on the primary MySQL server with appropriate permissions. The script `3-create_replica_user.sh` handles this task.

## Task 4: Setup a Primary-Replica infrastructure using MySQL

This task involves setting up replication between the primary MySQL server (web-01) and the replica server (web-02). The configurations for both servers are provided in the files `4-mysql_configuration_primary` and `4-mysql_configuration_replica`. The setup script `4-setup_replication.sh` accomplishes the replication setup.

## Task 5: MySQL backup

A Bash script `5-mysql_backup.sh` is provided to generate a MySQL dump, compress it, and create a backup archive with the specified format.

## How to Use

1. Clone this repository to your local machine:

```bash
git clone <repository-url>
```

2. Navigate to the repository directory:

```bash
cd 0x14-mysql
```

3. Execute the desired script(s) according to the task requirements:

```bash
./<script-name>.sh
```
Replace <script-name> with the name of the script you want to execute.

## Author

Naoufal Hadra

Feel free to customize this README file further according to your project's specific requirements and conventions. If you have any questions or need further assistance, please let me know!
