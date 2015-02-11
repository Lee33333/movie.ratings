from flask import Flask, render_template, redirect, request
import model

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")


@app.route("/new_user")
def new_user():
    pass
    return render_template("new_user.html")

@app.route("/login")
def login():
    pass
    return render_template("login.html")

@app.route("/movie_list", methods=["POST"])
def movie_list():

    email = request.form.get("email")
    password = request.form.get("password")
    age = int(request.form.get("age"))
    zipcode = request.form.get("zipcode")

    new_user = model.User(email=email, password=password, age=age, zipcode=zipcode)
    model.session.add(new_user)
    model.session.commit()

    return render_template("movie_list.html", )

if __name__== "__main__":
    app.run(debug = True)