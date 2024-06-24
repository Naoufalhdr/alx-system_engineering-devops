# 0x1B. Web Stack Debugging #4

## Description

This project focuses on debugging a web stack, specifically an Nginx web server under heavy load. We are using Puppet manifests to resolve issues related to high request failure rates and user file limits.

## Requirements

- All files are interpreted on Ubuntu 14.04 LTS.
- Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors.
- Files will be checked with Puppet v3.4.

## Install puppet-lint

```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```

## Tasks

### 0. Sky is the limit, let's bring that limit higher

#### Description:

In this task, we are testing the performance of our Nginx web server setup under pressure using ApacheBench (ab). Initially, the server fails to handle the load, resulting in a high number of failed requests. The goal is to debug and fix the setup to achieve zero failed requests.

#### Steps to Reproduce:

1. Run ApacheBench to test the server:

```bash
ab -c 100 -n 2000 http://localhost/
```

2. Apply the Puppet manifest to fix the issue:

```bash
puppet apply 0-the_sky_is_the_limit_not.pp
```

3. Run ApacheBench again to verify the fix:

```bash
ab -c 100 -n 2000 http://localhost/
```

**File:** `0-the_sky_is_the_limit_not.pp`

### 1. User Limit

#### Description:

In this task, we are addressing the issue where the `holberton` user encounters "Too many open files" errors. The solution involves modifying the OS configuration to increase the limit on the number of open files.

#### Steps to Reproduce:

1. Log in as the holberton user:

```bash
su - holberton
```

2. Verify the current file limit and observe the error messages.

3. Apply the Puppet manifest to fix the issue:

```bash
puppet apply 1-user_limit.pp
```

4. Log in as the holberton user again and verify the fix:

```bash
su - holberton
ulimit -n
```

**File:** `1-user_limit.pp`
