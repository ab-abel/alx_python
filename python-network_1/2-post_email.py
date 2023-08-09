'''
This is a python script that takse URL and send a request to the URL
'''
import sys
import requests

def post_email(email):
    '''
    request Url and return the headers X_request-id
    '''
    print("Your email is: {}".format(email[2]))

if __name__ == "__main__":
    cmd_input = []
    for i in range(0, len(sys.argv)):
        cmd_input.append(str(sys.argv[i]))
    post_email(cmd_input)

