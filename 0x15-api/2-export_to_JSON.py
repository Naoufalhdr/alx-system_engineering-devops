#!/usr/bin/python3
"""
This script fetches and displays TODO list progress for a given employee ID
using a REST API.
"""
import json
import requests
import sys


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
        # Fetch user data
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()
        username = user_data.get("username")

        # Fetch TODOS list data
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        # Prepare data to be written to JSON file
        user_todo_list = {
            str(employee_id): [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            } for task in todos_data]
        }

        # Write TODOS list data to a json file
        with open(f"{employee_id}.json", "w") as json_file:
            json.dump(user_todo_list, json_file)

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        return
    except ValueError as json_err:
        print(f"JSON decoding error: {json_err}")
        return


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
