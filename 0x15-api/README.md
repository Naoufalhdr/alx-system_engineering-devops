# API Project

## Overview

This project involves creating Python scripts to interact with a REST API to fetch and process employee data. The project aims to teach the use of APIs, JSON and CSV data formats, and proper Python coding styles. The scripts developed will gather data from an API and export it to various formats such as CSV and JSON.

## Concepts Covered

- **API:** Application Programming Interface
- **REST API:** Representational State Transfer API
- **Microservices:** Architectural style that structures an application as a collection of loosely coupled services
- **CSV Format:** Comma-Separated Values format for data
- **JSON Format:** JavaScript Object Notation format for data
- **Pythonic Code Style:** Writing code that follows the conventions and idioms of the Python language

## Learning Objectives

By the end of this project, you should be able to explain:

- Why Bash scripting is not suitable for certain tasks
- What an API is and its importance
- What a REST API is and how it works
- What microservices are
- The CSV and JSON data formats
- How to write Python code following the Pythonic style guide

## Requirements

- Python 3.8.5 or later
- Use of urllib or requests module for HTTP requests
- Scripts should be executable
- Proper organization of imported libraries
- Adherence to PEP8 Python style guide

## Tasks

### 0. Gather Data from an API

**Script:** 0-gather_data_from_an_API.py

This script fetches information about an employee's TODO list progress from the API and displays it in a specified format.

**Usage:** python3 0-gather_data_from_an_API.py <employee_id>

### 1. Export to CSV

**Script:** 1-export_to_CSV.py

This script extends the previous task by exporting the employee's TODO list data to a CSV file.

**Usage:** python3 1-export_to_CSV.py <employee_id>

### 2. Export to JSON

**Script:** 2-export_to_JSON.py

This script extends the first task by exporting the employee's TODO list data to a JSON file.

**Usage:** python3 2-export_to_JSON.py <employee_id>

### 3. Dictionary of List of Dictionaries

**Script:** 3-dictionary_of_list_of_dictionaries.py

This script gathers TODO list data for all employees and exports it to a JSON file in a specific format.

**Usage:** python3 3-dictionary_of_list_of_dictionaries.py

## Examples

### Example Output for Task 0

```bash
$ python3 0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks(8/20):
     distinctio vitae autem nihil ut molestias quo
     voluptas quo tenetur perspiciatis explicabo natus
     aliquam aut quasi
     veritatis pariatur delectus
     nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
     repellendus veritatis molestias dicta incidunt
     excepturi deleniti adipisci voluptatem et neque optio illum ad
     totam atque quo nesciunt
```

### Example CSV Output for Task 1

```csv
"2","Antonette","False","suscipit repellat esse quibusdam voluptatem incidunt"
"2","Antonette","True","distinctio vitae autem nihil ut molestias quo"
"2","Antonette","False","et itaque necessitatibus maxime molestiae qui quas velit"
"2","Antonette","False","adipisci non ad dicta qui amet quaerat doloribus ea"
```

### Example JSON Output for Task 2

```json
{
    "2": [
        {"task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": false, "username": "Antonette"},
        {"task": "distinctio vitae autem nihil ut molestias quo", "completed": true, "username": "Antonette"},
        ...
    ]
}
```

### Setup

1. Ensure Python 3.8.5 or later is installed on your system.
2. Clone the repository to your local machine.
3. Navigate to the project directory.
4. Run the scripts using the provided examples or custom employee IDs.

### References

- What is an API?
- REST API
- Microservices
- CSV Format
- JSON Format
- PEP8 Python Style Guide

This README provides a comprehensive guide to the tasks and scripts in this project, ensuring you understand the requirements and how to use the scripts effectively.
