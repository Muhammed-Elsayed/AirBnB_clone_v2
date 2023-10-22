#!/usr/bin/python3
"""List of"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """list all sorted list"""
    sortedlist = sorted(storage.all(
        State).values(), key=lambda x: x.name)

    return render_template("7-states_list.html", sortedlist=sortedlist)


@app.teardown_appcontext
def teardown(exc):
    """terminate sql alchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
