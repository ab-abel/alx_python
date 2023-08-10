'''
This is a python script that takse URL and send a request to the URL
'''
import sys
import requests


'''
request Url and return the headers X_request-id
'''
url = "http://0.0.0.0:5000/search_user"





if str(sys.argv[1]) is not None:
    letter = str(sys.argv[1])
    if letter:
        q=letter
    else:
        q=''
else:
        print("No result")
req = requests.post(url, q=q)
# print("[{}] {}".format(req.text))

# print(req.json)
# if isinstance(res_json, (dict,list)):
print("[{}] {}".format(req.json.id, req.json.name))
# elif res_json is None:
#     print("No result")
# except:
#     print("Not a valid JSON")

