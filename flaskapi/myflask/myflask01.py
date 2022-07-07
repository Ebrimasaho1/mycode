#!/usr/bin/python3

from flask import Flask

# app represents the entire website
app = Flask(__name__)

# decorator
@app.route("/")
def hello_world():
    return "Hello world!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
    # 2224 = aux1
    # 2225 = aux2
