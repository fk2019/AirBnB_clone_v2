#!/usr/bin/python3
"""Start a Flask web app
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_route():
    """Display Hello HBNB in / route"""
    return ("Hello HBNB!")
