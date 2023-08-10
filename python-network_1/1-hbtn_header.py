'''
This is a python script that takse URL and send a request to the URL
'''
import sys
import requests

def request_url(url):
    '''
    request Url and return the headers X_request-id
    '''
    url = str(sys.argv[1])
    request_url(url)

    url_to_str = "{}".format(url)
    req = requests.get(url_to_str)
    print(req.headers["X-Request-Id"])

