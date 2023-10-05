'''
A python script that uses the REST API for a given employee ID
returns information about his/her TODO list progress.
'''

import json
import requests
import sys


def data_to_json(user_id):
    """
    Fetches the employee's details and TODO list using the
    provided API endpoints,
    exports the informationto a JSON file.

    >>> data_to_json(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    
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



'''
A python script that uses the REST API for a given employee ID
returns information about his/her TODO list progress.
'''

import json
import requests
import sys

if __name__=='__main__':
    employee_id = sys.argv[1]
    api_request = requests.get("https://jsonplaceholder.typicode.com/users/%7B%7D".format(employee_id))
    api_request1 = requests.get("https://jsonplaceholder.typicode.com/users/%7B%7D/todos".format(employee_id))
    data = api_request.text
    pjson = json.loads(data)
    data1 = api_request1.text
    pjson1 = json.loads(data1)

    name_info = pjson['username']

    filename = "{}.json".format(employee_id)

    # Create the dictionary structure
    result = {
        employee_id: [{
            "task": item["title"],
            "completed": item["completed"],
            "username": name_info
        } for item in pjson1]
    }

    # export data to json file

    with open(filename, "w") as outfile:
        json.dump(result, outfile)