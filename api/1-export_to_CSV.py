'''
This module export content from an api into
a csv file defined on creation
    return : csv
'''
import csv
import requests
import sys

if __name__=='__main__':
    user_id = sys.argv[1]

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)

    user_data = requests.get(user_url).json()
    todo_data = requests.get(todo_url).json()

    filename = "{}.csv".format(user_id)

    with open(filename, 'w') as file:
        writter = csv.writer(file, quoting = csv.QUOTE_ALL)
        for task in todo_data:
            writter.writerow([user_id, str(user_data['name']),task['completed'], task['title']])