# dionysus

import random
import string

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """
    """

    return "<h1>Dionysus</h1>"


@app.route("/<int:length>")
def random_password(length):
    """
    """

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = "123456789"
    symbols = "[]{}()*;/,._-"
    characters = lower + upper + numbers + symbols
    password_length = length
    password = str("".join(random.sample(characters, password_length)))
    return password


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

