from flask import Flask, render_template, redirect, request, session
import model

app = Flask(__name__)
app.secret_key = '\xf5!\x07!qj\xa4\x08\xc6\xf8\n\x8a\x95m\xe2\x04g\xbb\x98|U\xa2f\x03'

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


@app.route("/authenticate", methods=["POST"])
def authenticate():
    email = request.form.get("email")
    password = request.form.get("password")
    user_in_db = model.get_user(email, password)

    if user_in_db == False:
        return redirect("/login")

    else:
        user_id = user_in_db.id
        print user_id
        session["current_user"] = user_id
        print session["current_user"]
        return render_template("authenticate.html")



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