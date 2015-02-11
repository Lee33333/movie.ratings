import model
import csv
from datetime import datetime

def load_users(session):
    # use u.user
    with open('seed_data/u.user', 'rb') as user_file:
        reader = csv.reader(user_file, delimiter='|')
        for row in reader:
            user = model.User(age=row[1], zipcode=row[4])
            session.add(user)
        session.commit()



def load_movies(session):
    # use u.item
    with open('seed_data/u.item', 'rb') as movie_file:
        reader = csv.reader(movie_file, delimiter='|')
        for row in reader:
            name = row[1]
            name = name.decode("latin-1") 
            released_string = row[2]
            print released_string
            if released_string != '':
                print "if"
                released_at = datetime.strptime(released_string, "%d-%b-%Y")
            else:
                print "else"
                released_at = None
            movie = model.Movie(name=name, released_at=released_at, imdb_url=row[4])
            session.add(movie)
        session.commit()

def load_ratings(session):
    # use u.data
    with open('seed_data/u.data', 'rb') as rating_file:
        reader = csv.reader(rating_file, delimiter='\t')
        for row in reader:
            rating = model.Rating(movie_id=row[1], user_id=row[0], rating=row[2])
            session.add(rating)
        session.commit()






def main(session):
    # You'll call each of the load_* functions with the session as an argument
    load_ratings(session)
    load_movies(session)
    load_users(session)

if __name__ == "__main__":
    s= model.connect()
    main(s)
