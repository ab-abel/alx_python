'''
Write a script that starts a Flask web application:
'''
# import flask module
from flask import Flask


# define a flask instance
app = Flask(__name__)
# set strict_s;ashes flag to fals
# for every route
app.url_map.strict_slashes = False

# create a route for index
@app.route('/')
# a function for
def hello():
    return "Hello HBNB!"
