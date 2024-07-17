#!/usr/bin/env python3
'''Basic flask app set up'''
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"])
def welcome():
    """get route to return a welcome message.
    """
    return jsonify({"message": "Bienvenue"})


if __name__ = "__main__":
    app.run(host="0.0.0.0", port="5000")
