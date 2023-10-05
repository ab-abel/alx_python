'''
DOc strings
'''
import csv

import requests
import sys
import json

todo_url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos'

try:
    csv_data = []
    user_id = 0
    req = requests.get(todo_url) 
    results = json.loads(req.text)
    for result in results:
        users = requests.get(f"https://jsonplaceholder.typicode.com/users/{result['userId']}")
        user = json.loads(users.text)
        csv_data.append([result['userId'], user['username'], result['completed'], result['title']]) 
        user_id = result['userId']

    filename = f"{str(sys.argv[1])}.csv"
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)

            # writer.writerow([result['userId'], user['username'], result['completed'], result['title']])
except TimeoutError:
    print("connection timed out")