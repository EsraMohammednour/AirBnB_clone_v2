#!/usr/bin/python3
'''Starts a Flask web application'''
from flask import Flask
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


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    ''' Return wellome massege'''
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
