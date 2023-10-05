'''
This module export content from an api into
a csv file defined on creation
    return : csv
'''
import csv
import os
import requests
import sys

user_id = str(sys.argv[1])

user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)

user_data = requests.get(user_url).json()
todo_data = requests.get(todo_url).json()

filename = "{}.csv".format(user_id)

with open(filename, 'w', newline='') as file:
    writter = csv.writer(file, quoting = csv.QUOTE_ALL)
    for task in todo_data:
        writter.writerow([user_id, str(user_data['username']),task['completed'], task['title']])

username = user_data['username']
id=user_id
flag = 0
with open(str(id) + ".csv", 'r') as f:
    for line in f:
        # print(line)
        if not line == '\n':
            if not str(id) in line:
                print("User ID: Incorrect / ", end='')
                flag = 1
            if not str(username) in line:
                print(str(username))
        #         print("Username: Incorrect")
        #         flag = 1

if flag == 0:
    print("User ID and Username: OK")
