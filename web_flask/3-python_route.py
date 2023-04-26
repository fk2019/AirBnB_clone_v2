#!/usr/bin/python3
"""Start a Flask web app that listens on 0.0.0.0
   port 5000
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Display Hello HBNB in / route"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hnbn_route():
    """Display HBNB in /hbnb route"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Display C followed by text variable"""
    return ("C %s" % text.replace('_', ' '))


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Display Python followed by text variable"""
    return ("Python %s" % text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
