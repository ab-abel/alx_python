'''
This is a python script that takse URL and send a request to the URL
'''
import sys
import requests


'''
request Url and return the headers X_request-id
'''
url = "http://0.0.0.0:5000/search_user"

if (sys.argv[1]):
    post_data ={'q':sys.argv[1]}
else: 
    post_data = {'q':''}

req = requests.post(url, data=post_data)
if req.status_code == 200:
    print("#####")
    print(req.text['id'])
    print(req.text['name'])
#     result = req.text
#     print("{}".format(result))
else:
    print("No result")
    
