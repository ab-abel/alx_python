'''
This is a python script that takse URL and send a request to the URL
'''
import sys
import requests


'''
request Url and return the headers X_request-id
'''
url = "http://0.0.0.0:5000/search_user"



if str(sys.argv[1]) is None:
    print("No result")
else:
    letter = str(sys.argv[1])
    if letter:
        q = letter
    else:
        q = ''
    
req = requests.post(url, json=q)
if req.status_code == 200:
    result = req.json()
    print("[{}] {}".format(result['id'],result['name']))
else:
    print("No result")
    

