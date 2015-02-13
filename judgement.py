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
    return render_template("all_users.html", all_users=all_users)



@app.route("/user/<int:user_id>")
def get_user(user_id):
    all_movies = model.get_movies_by_user(user_id)

    return render_template("movie_list.html", all_movies=all_movies)



@app.route("/movie/<int:movie_id>", methods=["POST", "GET"])
def get_movie(movie_id):
    all_ratings = model.get_ratings_by_movie(movie_id)

    if session.get("current_user"):
        existing_rating = model.get_rating_by_user(session["current_user"], movie_id)
        
        if existing_rating == None:

            # add render template so that if a user is logged in but there is no existing rating they have the capacity to add a rating

    #     if existing_rating:
    #         #show rating
    #         return render_template("rating_list.html", all_ratings=all_ratings, existing_rating=existing_rating)


    #     else:
    #         rating = int(request.form.get("number"))
    #         new_rating = model.Rating(user_id=session["current_user"], movie_id=movie_id, rating=rating)
    #         model.session.add(new_rating)
    #         model.session.commit()
    #         print "HEEEEEEEEEEEEEEEEEEEEELLLLLLLLLLLLLLLLLLLLLLLLLLLLOOOOOOOOOOOOOO", new_rating

    #         return render_template("rating_list.html", all_ratings=all_ratings)
    # else:

    return render_template("rating_list.html", all_ratings=all_ratings)


if __name__== "__main__":
    app.run(debug = True)