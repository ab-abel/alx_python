'''
This module export content from an api into
a JSON file defined on creation
    filename: USER_ID.json
'''
import json
import requests
import sys

# get input from user
user_id = str(sys.argv[1])

# format url with input from user
user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)

# request data frm todo and user api
user_data = requests.get(user_url).json()
todo_data = requests.get(todo_url).json()

# creat a json data from the todo and user object
json_data = {
    user_id :[
        {
            "task":task['title'],
            "completed":task['completed'],
            "username":user_data['username'],
        }
        for task in todo_data
    ]
}

# Write to JSON file name filename
filename = f"{user_id}.json"

# open the file and overwrite it content with w
def write_to_json(json_data):
    '''
    a function that write a given json data to a json file
        param : json data
        return : none
    '''
    with open(filename, 'w') as file:
        json.dump(json_data, file, indent=2)

# function call 
write_to_json(json_data)