#!/usr/bin/python3
'''Starts a Flask web application'''
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    ''' Return wellome massege'''
    return "Hello HBNB!"


@app.route('/c/<text>', strict_slashes=False)
def C_is_fun(text):
    ''' Return the massege'''
    no_underscore = text.replace('_', ' ')
    return f"C {no_underscore}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Return the massege"""
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Return the massege"""
    return f"{n} is a number"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    ''' Return wellome massege'''
    return "HBNB"

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''return html file'''
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
