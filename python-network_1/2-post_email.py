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
cmd_input = []

try:
    for i in range(0, len(sys.argv)):
        cmd_input.append(str(sys.argv[i]))
    data = {
        'email':cmd_input[2]
    }
    response = requests.post(cmd_input[1], data=data )
    print("{}".format(response.text))
except:
    print(None)