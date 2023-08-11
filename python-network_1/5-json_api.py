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
    q= sys.argv[1]
else: 
    q=''

req = requests.post(url, json=q)

print(req.headers)
print("#####")
print(req.json)
print("#####")
print(req.content)
print("#####")
print(req.text)
# if req.status_code == 200:
#     result = req.text
#     print("{}".format(result))
# else:
#     print("No result")
    
