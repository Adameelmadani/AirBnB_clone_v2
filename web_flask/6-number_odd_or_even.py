#!/usr/bin/python3
"""
This is our module
"""
from flask import Flask
from flask import render_template

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


@app.route('/number/<int:n>')
def number_n(n):
    """
    Display n is number only if n is int
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def number_temp(n):
    """
    Display an html page
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_even(n):
    """
    Display an html page if n is even or odd
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
