import datetime

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
# first app
# def hello_world():
# return 'Hello, World!'

#  second app add dynamic route

# @app.route('/<string:name>')
# def hello(name):
# name = name.capitalize()
# return f"Hello, {name}"
# third app --> uses template to render html
# change index for posting
def index():
    # headline = "Jacqueline Hendricks"
    # return render_template("index1.html", headline=headline)
    return render_template("index.html")


# add hello to use forms
@app.route('/hello', methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)


@app.route("/bye")
def bye():
    headline = "Goodbye"
    return render_template("index1.html", headline=headline)


@app.route("/my")
def birthday():
    now = datetime.datetime.now()
    birthday = now.month == 2 and now.day == 3
    # override for testing
    # birthday = True
    return render_template("birthday.html", birthday=birthday)


@app.route("/loop")
def loop():
    names = ["Robert", "Jacqueline", "Mary Lee", "David"]
    return render_template("loop.html", names=names)


@app.route("/more")
def more():
    return render_template("more1.html")
