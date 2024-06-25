# 0x1A. Application Server

## Description

This project is focused on building an application server capable of handling multiple client connections concurrently. The server is designed to manage various HTTP requests and responses using a multi-threaded approach, ensuring efficient handling of client interactions.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Usage](#usage)
- [Features](#features)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [Tasks](#Tasks)
- [License](#license)

## Requirements

To run the application server, you need:
- Python 3.x
- Flask
- Requests library
- SQLite3 (for database operations)
- SQLAlchemy

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/0x1A-application-server.git
cd 0x1A-application-server
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the server:

```bash
python app.py
```

4. Once the server is running, you can access it through `http://localhost:5000` in your web browser.

## Features

- Multi-threaded server architecture
- HTTP request handling (GET, POST, PUT, DELETE)
- SQLite database integration for persistent storage
- RESTful API design
- Error handling and logging

## How It Works

The application server utilizes Python's Flask framework to handle HTTP requests and responses. It supports CRUD (Create, Read, Update, Delete) operations through RESTful API endpoints. SQLite is used as the database backend to store and retrieve data efficiently. The server is designed to be scalable and robust, capable of managing concurrent client connections using threading.

## Tasks

### 0. Set up development with Python (mandatory)

Let’s serve what you built for AirBnB clone v2 - Web framework on web-01. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.

Requirements:

- Make sure that task #3 of your SSH project is completed for web-01. The checker will connect to your servers.
- Install the net-tools package on your server: `sudo apt install -y net-tools`
- Git clone your `AirBnB_clone_v2` on your web-01 server.
- Configure the file `web_flask/0-hello_route.py` to serve its content from the route /airbnb-onepage/ on port 5000.
- Your Flask application object must be named `app` (This will allow us to run and check your code).

### 1. Set up production with Gunicorn (mandatory)

Now that you have your development environment set up, let’s get your production application server set up with Gunicorn on web-01, port 5000.

Requirements:

- Install Gunicorn and any other libraries required by your application.
- The Flask application object should be called `app`. (This will allow us to run and check your code)
- You will serve the same content from the same route as in the previous task.
- In order to check your code, the checker will bind a Gunicorn instance to port 6000, so make sure nothing is listening on that port.

### 2. Serve a page with Nginx (mandatory)

Building on your work in the previous tasks, configure Nginx to serve your page from the route /airbnb-onepage/.

Requirements:

- Nginx must serve this page both locally and on its public IP on port 80.
- Nginx should proxy requests to the process listening on port 5000.
- Include your Nginx config file as `2-app_server-nginx_config`.

### 3. Add a route with query parameters (mandatory)

Building on what you did in the previous tasks, let’s expand our web application by adding another service for Gunicorn to handle.

Requirements:

- Nginx must serve this page both locally and on its public IP on port 80.
- Nginx should proxy requests to the route `/airbnb-dynamic/number_odd_or_even/(any integer)` to the process listening on port 5001.
- Include your Nginx config file as `3-app_server-nginx_config`.

### 4. Let's do this for your API (mandatory)

Let’s serve what you built for AirBnB clone v3 - RESTful API on web-01.

Requirements:

- Git clone your `AirBnB_clone_v3.`
- Setup Nginx so that the route `/api/` points to a Gunicorn instance listening on port 5002.
- Nginx must serve this page both locally and on its public IP on port 80.
- To test your setup you should bind Gunicorn to `api/v1/app.py`.
- Upload your Nginx config file as `4-app_server-nginx_config`.

### 5. Serve your AirBnB clone (mandatory)

Let’s serve what you built for AirBnB clone - Web dynamic on web-01.

Requirements:

- Git clone your `AirBnB_clone_v4.`
- Your Gunicorn instance should serve content from `web_dynamic/2-hbnb.py` on port 5003.
- Setup Nginx so that the route `/` points to your Gunicorn instance.
- Setup Nginx so that it properly serves the static assets found in `web_dynamic/static/`.
- Nginx must serve this page both locally and on its public IP and port 5003.
- Make sure to pull up your Developer Tools on your favorite browser to verify that you have no errors.
- Upload your Nginx config as `5-app_server-nginx_config`.

### 6. Deploy it! (#advanced)

Once you’ve got your application server configured, you want to set it up to run by default when Linux is booted.

Requirements:

- Write a systemd script which starts a Gunicorn process to serve the same content as the previous task (`web_dynamic/2-hbnb.py`).
- The Gunicorn process should spawn 3 worker processes.
- The process should log errors in `/tmp/airbnb-error.log`.
- The process should log access in `/tmp/airbnb-access.log`.
- The process should be bound to port 5003.
- Your systemd script should be stored in the appropriate directory on web-01.
- Make sure that you start the systemd service and leave it running.
- Upload `gunicorn.service` to GitHub.

### 7. No service interruption (#advanced)

Write a simple Bash script to reload Gunicorn in a graceful way.

## Contributing

Contributions are welcome! If you want to contribute to this project, follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature`)
6. Create a new Pull Request

Please ensure that your code adheres to the project's coding standards and includes appropriate documentation and test cases.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
