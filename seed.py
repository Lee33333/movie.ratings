import model
import csv

def load_users(session):
    # use u.user
    pass

def load_movies(session):
    # use u.item
    pass

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

if __name__ == "__main__":
    s= model.connect()
    main(s)
