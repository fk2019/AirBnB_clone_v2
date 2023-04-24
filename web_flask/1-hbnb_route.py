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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
