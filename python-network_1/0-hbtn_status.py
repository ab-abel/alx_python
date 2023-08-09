'''
This modele uses the requests moduleno  to
fetch and get requests from  alu-intranet
'''
import requests
# import json

req = requests.get("https://alu-intranet.hbtn.io/status")


print("Body response:")
print(" - type: {}".format(type(req.text)))
print(" - content: {}".format(req.text))
# print(req.content)
