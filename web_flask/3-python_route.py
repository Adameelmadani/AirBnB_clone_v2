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


@app.route('/c/<text>')
def c_text(text):
    """
    Display c text
    """
    text2 = "C " + text.replace("_", " ")
    return text2

@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """
    Display python text
    """
    text2 = "Python " + text.replace("_", " ")
    return text2


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
