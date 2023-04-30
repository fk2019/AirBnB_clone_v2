#!/usr/bin/python3
"""Start a Flask web app that listens on 0.0.0.0
   port 5000 and use `storage` for fetching data from   engine
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Terminate in each request the SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display HTML inside <BODY> tag the list of
    statesand cities in ascending order"""
    states = storage.all(State)
    return (render_template('8-cities_by_states.html', states=states))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
