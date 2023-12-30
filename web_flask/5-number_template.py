#!/usr/bin/python3
"""This is to create more routes and display C and additional text"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello hbnb!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB!"


@app.route("/c/<text>", strict_slashes=False)
def char(text):
    form_text = text.replace("_", " ")
    return f'C {form_text}'


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pyth(text):
    form_text = text.replace("_", " ")
    return f'Python {form_text}'


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return "%i is a number" % n


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_template(n):
    return "<BODY><H1>Number: %i</H1></BODY>" % n


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
