# App entry
from flask import Flask, render_template, request

app = Flask(__name__)


# root or homepage
@app.route("/")
def index():
    return render_template("index.html")


# POST METHOD
@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)
