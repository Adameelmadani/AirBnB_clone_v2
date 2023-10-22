#!/usr/bin/python3
"""
This is our module
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from os import getenv

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def states_list():
    """
    Returns html page of states list
    """
    states = storage.all('State').values()
    s = getenv("HBNB_TYPE_STORAGE")
    return render_template('8-cities_by_states.html', states=states, storage_t=s)


@app.teardown_appcontext
def teardown(exception):
    """
    Close session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
