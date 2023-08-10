'''
This is a python script that takse URL and send a request to the URL
'''
import sys
import requests

letter = str(sys.argv[1])
'''
request Url and return the headers X_request-id
'''
url = "http://0.0.0.0:5000/search_user"

data = {
    'email':cmd_input[2]
}

if letter:
    data = {'q' : letter}
else:
    data = {'q':""}

try:
    req = requests.post(url, data = data)
    res_json = req.json()
    if isinstance(res_json, (dict,list)):
        print("[{}] {}".format(res_json.id, res_json.name))
    elif res_json is None:
        print("No result")
except:
    print("Not a valid JSON")

