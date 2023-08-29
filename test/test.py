from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    return "Hello HBNB"

@app.route('/hbnb')
def hbnb():
    return "HBNB"

@app.route('/c/<text>')
def c_is_fun(text):
    return f"C {escape(text.replace('_', ' '))}"

if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0')
