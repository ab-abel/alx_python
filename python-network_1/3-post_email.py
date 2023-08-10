'''
This is a python script that takse URL and send a request to the URL
'''
import sys
import requests


cmd_input = []
for i in range(0, len(sys.argv)):
    cmd_input.append(str(sys.argv[i]))

'''
this function takes a sys input and return the email body
'''

response = requests.post(cmd_input[1], cmd_input[2])
print("Your email is: {}".format(response.text))
