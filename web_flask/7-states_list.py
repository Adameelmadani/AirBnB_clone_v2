#!/usr/bin/python3
"""
This is our module
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """
    Returns html page of states list
    """
    return render_template('7-states_list.html',
            states=storage.all('State').values())

@app.teardown_appcontext
def teardown():
    """
    Close session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
