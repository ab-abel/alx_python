'''
This is a python script that takse URL and send a request to the URL
'''
import sys
import requests


'''
request Url and return the headers X_request-id
'''
url = "http://0.0.0.0:5000/search_user"



# print()
# kwargs = {'q' : str(sys.argv[1])}
# }
    
req = requests.post(url, str(sys.argv[1]))
print(req)
# if req.status_code == 200:
#     result = req.text
#     print("{}".format(result))
# else:
#     print("No result")
    

