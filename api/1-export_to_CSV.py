'''
DOc strings
'''
import csv
import json
import requests
import sys

todo_url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos'

req = requests.get(todo_url) 
results = json.loads(req.text)

csv_data = []
user_id = 0
for result in results:
    users = requests.get(f'https://jsonplaceholder.typicode.com/users/{result['userId']}')
    user = json.loads(users.text)
    csv_data.append([result['userId'], user['username'], result['completed'], result['title']]) 
    user_id = result['userId']

filename = f"{user_id}.csv"
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)

        # writer.writerow([result['userId'], user['username'], result['completed'], result['title']])