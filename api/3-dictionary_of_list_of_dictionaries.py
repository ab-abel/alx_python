"""
This is a python module that takes id from d user
and send a request to the Url. the response is
formatted and save to a json file.

param:
    filename: string
    user_id : string
    data_to_json : function
"""
import json
import requests
import sys


def data_to_json(user_id):
    """
    Fetches the employee's details and TODO list using the
    provided API endpoints,
    exports the informationto a JSON file.

    Parameters:
    - employee_id (int): The ID of the employee.

    Returns:
    None
    """
    # format url with input from user
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'\
    .format(user_id)
    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'\
    .format(user_id)

    # request data frm todo and user api
    user_data = requests.get(user_url).json()
    todo_data = requests.get(todo_url).json()

    # creat a json data from the todo and user object
    json_data = {
        user_id : [ {
                "username": user_data['username'],"task": task['title'], "completed": task['completed'],
            }
            for task in todo_data
        ]
    }

    # Write to JSON file name filename
    filename = "todo_all_employees.json"

    # open the file and overwrite it content with w
    with open(filename, 'w') as file:
        json.dump(json_data, file, indent=2)

# function call
data_to_json(sys.argv[1])
