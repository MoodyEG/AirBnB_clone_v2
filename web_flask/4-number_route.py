#!/usr/bin/python3
""" Main Moduel """
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Main page """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ HBNB page """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """ C page """
    return "C " + text.replace("_", " ")


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python_route(text="is cool"):
    """ Python page """
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """ Number page """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
