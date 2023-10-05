'''
DOc strings
'''
import csv
import json
import os
import requests
import sys


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
    new_file_path = os.path.join(OUTPUT_DIR, str(filename))
    with open(new_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([result['userId'], user['username'], result['completed'], result['title']])
except TimeoutError:
    print("connection timed out")