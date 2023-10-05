'''
This module export content from an api into
a csv file defined on creation
    return : csv
'''

import json
import requests
import sys

user_id = str(sys.argv[1])

user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)

user_data = requests.get(user_url).json()
todo_data = requests.get(todo_url).json()

filename = "{}.csv".format(user_id)

json_data = {
        "user_id" :[
            {
            "task":task['title'],
            "completed":task['completed'],
            "username":user_data['username'],
            }
            for task in todo_data
    ]
}

# Write to JSON file
filename = f"{user_id}.json"
with open(filename, 'w') as file:
    json.dump(json_data, file, indent=2)
