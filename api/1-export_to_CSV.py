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


    
    for result in results:
        users = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(result['userId']))
        user = json.loads(users.text)
        
        open(f"{result['userId']}.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([result['userId'], user['username'], result['completed'], result['title']])