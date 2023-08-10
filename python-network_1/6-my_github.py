'''
modlue that use PAT to access the Git hub api
'''

import sys
import requests


username = str(sys.argv[1])
token = str(sys.argv[2])


url = f'https://api.github.com/users/{username}'

headers = {
    'Authorization' : f'Token {token}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    user_data = response.json()
    user_id = user_data['id']
    print(f"{user_id}")
else:
    print("f error: {response.status_code}")