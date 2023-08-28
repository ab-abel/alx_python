from glob import escape
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return request.url_for('')

@app.route('/<username>')
def hello_user(username):
    return f"Hello,  {escape(username)}"

