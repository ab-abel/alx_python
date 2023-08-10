'''
This modele uses the requests moduleno  to
fetch and get requests from  alu-intranet
'''
import requests


req = requests.get("https://alu-intranet.hbtn.io/status")
print("Body response:\n\t- type: {}\n\t- content: {}".format(type(req.text),req.text))
