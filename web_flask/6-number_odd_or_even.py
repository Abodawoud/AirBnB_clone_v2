#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display “HBNB!”"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text: str):
    """display C text!”"""
    return f'C {text.replace("_", " ")}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_text(text="is cool"):
    """display Python text!"""
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def n_text(n):
    """display n is number!”"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_template_even_or_odd(n):
    """Number: n is even|odd” inside the tag BODY"""
    if (n % 2 == 0):
        e_o = "even"
    else:
        e_o = "odd"
    return render_template('6-number_odd_or_even.html', number=n, e_o=e_o)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
