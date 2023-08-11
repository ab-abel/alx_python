'''
This is a python script that takse URL and send a request to the URL
'''
import sys
import requests


'''
request Url and return the headers X_request-id
'''
url = "http://0.0.0.0:5000/search_user"

try:
    if (sys.argv[1]):
        post_data ={'q':sys.argv[1]}
    else: 
        post_data = {'q':''}

    req = requests.post(url, data=post_data)
    if req.status_code == 200:
        
        data = '{}'.format(req.text)

        # Remove curly braces and split the string
        pairs = data[1:-2].split(',')

        # Create a dictionary from the key-value pairs
        result = {}
        for pair in pairs:
            key, value = pair.split(':')
            result[key.strip('"')] = value.strip('"')
        
        
        print(f"[{result['id']}] {result['name']}")

    else:
        print("No result")
        
except IndexError:
    print("No result")