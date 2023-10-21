#!/usr/bin/python3
"""
This is our module
"""
from flask import Flask

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """
    This is the root page
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
    This is the hbnb page
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
