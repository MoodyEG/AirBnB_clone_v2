#!/usr/bin/python3
""" Main Moduel """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list")
def states_list():
    """Displays a HTML page with a list of all 
    State objects in DBStorage sorted by name (A->Z)"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """Removes the current SQLAlchemy Session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
