#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def display_states():
    """
    Displays a HTML page with the list of all State objects present in DBStorage.
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def display_state_cities(id):
    """
    Displays a HTML page with the list of City objects linked to the specified State.
    """
    state = storage.get(State, id)
    if state is None:
        return render_template('9-states.html', not_found=True)
    else:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-states.html', state=state, cities=cities)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Removes the current SQLAlchemy Session.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

