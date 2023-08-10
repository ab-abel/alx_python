"""
module hbtn-header

hbtn-header based on Request and sys Library

hbtn-header is a requests, sys bases python script that take URL and send a request to the URL,
The value of this variable is different for each request.

Basic Usage: 

    >>> import requests
    >>> import sys

    >>> get url from terminal
    >>> sys.argv
    >>> send a request to the url using
    >>> requests.get(sys.argv)
    >>> return header information
    >>> using response.headers[''x-id]
    >>> display using print

Example:

    >>> py -m 1-hbtn_header.py https://intranet.hbtn.io

Import:
    sys, requests

Parameters:

    url - url of the requested page gotten from sys
    url_to_str - return a str from the url list
    req - get request to the specified url

Return:

    request headers x-request-Id
"""

import sys
import requests
response = requests.get(str(sys.argv[1]))
print(response.headers['X-Request-Id'])
