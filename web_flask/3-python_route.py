#!/usr/bin/python3
"""
A simple flask application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """This route returns hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """This route return HBNB"""
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """Returns 'C' followed by the text provided"""
    text = text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python")
@app.route("/python/")
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """Returns the text provided"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
