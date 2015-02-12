from flask import Flask, render_template, redirect, request, session, flash
import model

## OUR DATABSE ACCEPTS AGES AS NON INTEGERS AND MULTIPLES OF EMAILS FIXME

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
        flash("Please try again, we couldn't locate your information in the database")
        return redirect("/login")

    else:
        user_id = user_in_db.id
        session["current_user"] = user_id
        flash("Welcome")
        return render_template("authenticate.html")



@app.route("/add_user", methods=["POST"])
def movie_list():

    email = request.form.get("email")
    password = request.form.get("password")
    age = int(request.form.get("age"))
    zipcode = request.form.get("zipcode")

    new_user = model.User(email=email, password=password, age=age, zipcode=zipcode)
    model.session.add(new_user)
    model.session.commit()

    session["current_user"] = new_user.id

    flash("New account created!")

    return render_template("add_user.html", )



@app.route("/all_users")
def get_users():
    all_users = model.get_all_users()
    print all_users
    return render_template("all_users.html", all_users=all_users)


if __name__== "__main__":
    app.run(debug = True)