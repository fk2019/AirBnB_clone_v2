#!/usr/bin/python3
"""Start a Flask web app that listens on 0.0.0.0
   port 5000 and use `storage` for fetching data from   engine
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Terminate in each request the SQLAlchemy Session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display HTML inside <BODY> tag the list of state ctities
    in ascending order"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    amenity_l = []
    for value in amenities.values():
        amenity_l.append(value.name)
    amenity_l.sort()
    return (render_template('10-hbnb_filters.html', states=states, amenities=amenity_l))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
