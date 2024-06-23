# 0x17. Web Stack Debugging #3

## Overview

This project involves debugging a web stack, specifically a WordPress site running on a LAMP (Linux, Apache, MySQL, and PHP) stack. The main task is to identify and resolve issues causing an Apache server to return a 500 Internal Server Error, using `strace` for debugging and Puppet for automation.

## Background Context

Debugging complex software systems often requires more than just examining logs. In cases where logs are insufficient, diving deeper into the stack is necessary. This project helps you develop skills to debug web servers and automate fixes using Puppet.

WordPress is a widely used content management system that powers a significant portion of the web. Being proficient in managing and debugging WordPress on a LAMP stack is a valuable skill for any DevOps engineer.

## Concepts to Explore

- Web Server
- Web Stack Debugging

## Requirements

- All files will be interpreted on Ubuntu 14.04 LTS.
- All files should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- Puppet manifests must pass `puppet-lint` version 2.1.1 without errors.
- Puppet manifests must run without errors.
- The first line of Puppet manifests must be a comment explaining what the manifest is about.
- Puppet manifests files must end with the extension `.pp`.
- Files will be checked with Puppet v3.4.

## Installation

### Install puppet-lint

```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```

## Tasks

### 0. Strace is your Friend

**Objective:**

Using `strace`, find out why Apache is returning a 500 error. Fix the issue and automate the solution using Puppet.

**Hint:**

- `strace` can attach to a running process.
- Use `tmux` to run `strace` in one window and `curl` in another.

**Requirements:**

- The `0-strace_is_your_friend.pp` file must contain Puppet code.
- You can use any Puppet resource type for your fix.

**Example:**

```bash
root@e514b399d69d:~# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 24 Mar 2017 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html

root@e514b399d69d:~# puppet apply 0-strace_is_your_friend.pp
Notice: Compiled catalog for e514b399d69d.ec2.internal in environment production in 0.02 seconds
Notice: /Stage[main]/Main/Exec[fix-wordpress]/returns: executed successfully
Notice: Finished catalog run in 0.08 seconds
root@e514b399d69d:~# curl -sI 127.0.0.1:80
HTTP/1.1 200 OK
Date: Fri, 24 Mar 2017 07:11:52 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Link: <http://127.0.0.1/?rest_route=/>; rel="https://api.w.org/"
Content-Type: text/html; charset=UTF-8

root@e514b399d69d:~# curl -s 127.0.0.1:80 | grep Holberton
<title>Holberton &#8211; Just another WordPress site</title>
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Feed" href="http://127.0.0.1/?feed=rss2" />
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Comments Feed" href="http://127.0.0.1/?feed=comments-rss2" />
        <div id="wp-custom-header" class="wp-custom-header"><img src="http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg" width="2000" height="1200" alt="Holberton" /></div>  </div>
                            <h1 class="site-title"><a href="http://127.0.0.1/" rel="home">Holberton</a></h1>
        <p>Yet another bug by a Holberton student</p>
root@e514b399d69d:~#
```

## Repository

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x17-web_stack_debugging_3`
- File: `0-strace_is_your_friend.pp`

## Good Luck!

Debugging can be challenging but also rewarding. Remember to methodically test your assumptions, use the right tools, and document your process. With experience, you'll become adept at resolving even the most complex issues.
