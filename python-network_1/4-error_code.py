'''
This is a python script that takse URL and send a request to the Url
and display the response of the results.
'''
import sys
import requests


'''
This function send request using the url requests module

Parameters:
    url: the link to the url to send a request to

Return:
    return: the text response.

'''

req = requests.get(str(sys.argv[1]))
if req.status_code == 200:
    print(req.text)
elif req.status_code >= 400:
    print("Error code:{}".format(req.status_code))
