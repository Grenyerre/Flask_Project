import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/") # Browse to the root directory, then Flask triggers the function beneath.
def index():
    return render_template("index.html")


if __name__ == "__main__": # __main__ is the name of the default module in Python
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)