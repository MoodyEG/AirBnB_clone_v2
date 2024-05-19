#!/usr/bin/python3
""" Main Moduel """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Displays a HTML page with a list of all
    State objects in DBStorage sorted by name (A->Z)"""
    states = storage.all(State).values()
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def state(id):
    """Displays a HTML page with a list of all
    cities objects in DBStorage in the state sorted by name (A->Z)"""
    state = None
    for s in storage.all(State).values():
        if s.id == id:
            state = s
    return render_template("9-states.html", state=state, states=None)


@app.teardown_appcontext
def teardown(exception):
    """Removes the current SQLAlchemy Session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
