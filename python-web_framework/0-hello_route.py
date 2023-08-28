'''
Write a script that starts a Flask web application:
'''
# import flask module
from flask import Flask


# define a flask instance
app = Flask(__name__)
# set strict_s;ashes flag to false

# create a route for index
@app.route('/')
# a function for
def hello():
    '''
    a function definition that return
    a strin hello... on a get request 
    to a router page
    '''
    return "Hello HBNB!"

if __name__!='__main__':
    # for every route
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0')