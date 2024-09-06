import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
# Browse to the root directory, then Flask triggers the function beneath.
# The root decorator binds the index() function to itself, thus whenever that
# root is called, the function is called. This function is also called a 'view'.
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__": # __main__ is the name of the default module in Python
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)