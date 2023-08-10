import requests

# URL to which you want to send the POST request
url = 'https://alu-intranet.hbtn.io/status'

# JSON data to be sent in the POST request
json_data = {
    'username': 'myuser',
    'password': 'mypassword'
}

# Send a POST request with JSON data
response = requests.post(url, json=json_data)

# Print the response content
print("Response Content:")
print(response.json)
