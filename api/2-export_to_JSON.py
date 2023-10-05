#!/usr/bin/python3
"""
This is a python script that takse id from d user and send a request to the Url
and save the formatted response to a json file.
"""
import json
import requests
import sys


def data_to_json(user_id):
    """
        Fetches the employee's details and TODO list using the provided API endpoints,
        calculates the progress, and exports the information to a JSON file.

        Parameters:
        - employee_id (int): The ID of the employee.

        Returns:
        None
    """
    # format url with input from user
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)

    # request data frm todo and user api
    user_data = requests.get(user_url).json()
    todo_data = requests.get(todo_url).json()

    # creat a json data from the todo and user object
    json_data = {
        user_id : [ {
                "task":task['title'], "completed":task['completed'],
                "username":user_data['username'],
            }
            for task in todo_data
        ]
    }

    # Write to JSON file name filename
    filename = f"{user_id}.json"

    # open the file and overwrite it content with w

    with open(filename, 'w') as file:
        json.dump(json_data, file, indent=2)

# function call
data_to_json(sys.argv[1])