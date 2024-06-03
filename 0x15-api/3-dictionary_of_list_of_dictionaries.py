#!/usr/bin/python3
"""
This script fetches and exports TODO list progress for all employees
using a REST API, and stores the data in a JSON file.
"""
import json
import requests
import sys


def fetch_todo_list_progress():
    """
    Fetches TODO list progress for all employees and exports the data
    in JSON format to a file named 'todo_all_employees.json'.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/"

    try:
        # Fetch user data
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()

        # Dictionary to store data for all users
        user_dict = {}

        # Loop through each user
        for user in user_data:
            todos_url = f"{base_url}/todos?userId={user.get('id')}"
            username = user.get("username")

            # Fetch TODO list data for current user
            todos_response = requests.get(todos_url)
            todos_response.raise_for_status()
            todos_data = todos_response.json()

            # Prepare data for current user to be written to JSON file
            user_dict.update({
                str(user.get('id')): [{
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                } for task in todos_data]
            })

        # Write TODOS list data to a json file
        with open("todo_all_employees.json", "w") as json_file:
            json.dump(user_dict, json_file)

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
    fetch_todo_list_progress()
