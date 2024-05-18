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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
