#!/usr/bin/python3
"""Start a Flask web app that listens on 0.0.0.0
   port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display HTML inside <BODY> tag"""
    states = storage.all(State)
    state_list = []
    for value in states.values():
        state_list.append({value.id: value.name})
    return (render_template('7-states_list.html', state_list=state_list))


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
