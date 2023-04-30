#!/usr/bin/python3
"""Start a Flask web app that listens on 0.0.0.0
   port 5000 and use `storage` for fetching data from   engine
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Terminate in each request the SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display HTML inside <BODY> tag the list of states in ascending order"""
    states = storage.all(State)
    state_list = {}
    for value in states.values():
        state_list.update({value.id: value.name})
    state_list = dict(sorted(state_list.items(), key=lambda x: x[1]))
    return (render_template('7-states_list.html', state_list=state_list))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
