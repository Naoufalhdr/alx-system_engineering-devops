# 0x12. Web Stack Debugging #2

## Description

This project focuses on web stack debugging. We will work on ensuring that the web server, Nginx, runs under the proper user and implements best security practices.

## Requirements

- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A README.md file at the root of the folder of the project is mandatory
- All your Bash script files must be executable
- Your Bash scripts must pass Shellcheck without any error
- Your Bash scripts must run without error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what the script is doing

## Tasks

### 0. Run software as another user

**Task**:

Write a Bash script that accepts one argument and runs the whoami command under the user passed as an argument.

**Requirements:**

- The script should run the whoami command under the user passed as an argument
- Ensure to try your script by passing different users

**Example:**

```sh
root@ubuntu:~# whoami
root
root@ubuntu:~# ./0-iamsomeoneelse www-data
www-data
root@ubuntu:~# whoami
root
root@ubuntu:~#
```

***File:***

0-iamsomeoneelse

### 1. Run Nginx as Nginx

**Task:**

Fix the container so that Nginx is running as the nginx user.

**Requirements:**

- Nginx must be running as nginx user
- Nginx must be listening on all active IPs on port 8080
- You cannot use apt-get remove
- Write a Bash script that configures the container to fit the above requirements

**Example:**

```sh
root@ab6f4542747e:~# ps auxff | grep ngin[x]
nginx      884  0.0  0.0  77360  2744 ?        Ss   19:16   0:00 nginx: master process /usr/sbin/nginx
nginx      885  0.0  0.0  77712  2772 ?        S    19:16   0:00  \_ nginx: worker process
nginx      886  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      887  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      888  0.0  0.0  77712  3208 ?        S    19:16   0:00  \_ nginx: worker process
root@ab6f4542747e:~#
root@ab6f4542747e:~# nc -z 0 8080 ; echo $?
0
root@ab6f4542747e:~#
```

***File:*** 

1-run_nginx_as_nginx

### 2. 7 lines or less

***Task:***

Using what you did for task #1, make your fix short and sweet.

***Requirements:***

- Your Bash script must be 7 lines long or less
- There must be a new line at the end of the file
- You respect Bash script requirements
- You cannot use ;
- You cannot use &&
- You cannot use wget
- You cannot execute your previous answer file (Do not include the name of the previous script in this one)

***File:***

100-fix_in_7_lines_or_less

## Usage

To execute the scripts, you need to make them executable and run them with the appropriate arguments. For example:

```sh
chmod +x 0-iamsomeoneelse
./0-iamsomeoneelse www-data
```

## Author

Naoufal Hadra (Naoufalhdr)

## Acknowledgments

ALX SE program for providing this challenging project

