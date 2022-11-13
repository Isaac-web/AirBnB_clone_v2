#!/usr/bin/python3
"""
A minimum flask app
"""
from flask import Flask


app = Flask(__name__)
@app.route("/")
def index():
    """This route returns a Hello World page"""
    return "Hello HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
