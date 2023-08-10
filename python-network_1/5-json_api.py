'''
This is a python script that takse URL and send a request to the URL
'''
import sys
import requests

def request_url(letter):
    '''
    request Url and return the headers X_request-id
    '''
    url = "http://0.0.0.0:5000/search_user"
    if letter:
        q = letter
    else:
        q=""
    req = requests.post(url, q)

    try:
        res_json = req.json()
    except json.JSONDecodeError:
        print("Not a valid JSON")
  


if __name__ == "__main__":
    url = str(sys.argv[1])
    request_url(url)
