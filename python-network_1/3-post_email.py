'''
This is a python script that takse URL and send a request to the URL
'''
import sys
import requests

def post_email(email):
    '''
    this function takes a sys input and return the email body
    '''

    response = requests.post(email[1], email[2])
    print("Your email is: {}".format(response.text))

    

if __name__ == "__main__":
    cmd_input = []
    for i in range(0, len(sys.argv)):
        cmd_input.append(str(sys.argv[i]))
    post_email(cmd_input)

