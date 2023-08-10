'''
This is a python script that takse URL and send a request to the URL
Import sys and requests.
Import:
    sys, requests
Paaramters:
    url, gotten from sys
Return:
    request headers x-request-Id
'''
import sys
import requests

url = str(sys.argv[1])
url_to_str = "{}".format(url)
req = requests.get(url_to_str)
print(req.headers["X-Request-Id"])
