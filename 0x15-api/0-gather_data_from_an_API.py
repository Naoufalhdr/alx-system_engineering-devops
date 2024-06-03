#!/usr/bin/python3
"""
Fetches and displays TODO list progress for a given employee ID using
a REST API.
"""

import sys
import requests


def fetch_todo_list_progress(employee_id):
    """
    Fetches and displays TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()

        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        return
    except ValueError as json_err:
        print(f"JSON decoding error: {json_err}")
        return

    tasks = [task['title'] for task in todos_data if task['completed']]

    print(
            f"Employee {user_data['name']} is done with tasks("
            f"{len(tasks)}/{len(todos_data)}):"
            )

    for task in tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    fetch_todo_list_progress(employee_id)
