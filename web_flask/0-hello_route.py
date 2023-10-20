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
