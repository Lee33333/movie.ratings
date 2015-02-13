from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref


engine = create_engine("sqlite:///ratings.db", echo=True)
session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

Base = declarative_base()
Base.query = session.query_property()

### Class declarations go here
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    email = Column(String(64), nullable= True)
    password = Column(String(64), nullable=True)
    age = Column(Integer, nullable=True)
    zipcode = Column(String(15), nullable=True)

    def __repr__(self):
        return "<User id=%r, email=%s>" %(self.id, self.email)

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key = True)
    #id is auto generated, so potentially displaced all ids during data cleaning
    name = Column(String(100), nullable = False)
    released_at = Column(DateTime, nullable = True)
    imdb_url = Column(String(200), nullable = True)

    def __repr__(self):
        return "<Movie id=%d name = %s>" % (self.id, self.name)

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movies.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    rating = Column(Integer, nullable=False)

    user = relationship("User",
            backref=backref("ratings", order_by=id))

    movie = relationship("Movie",
            backref=backref("ratings", order_by=id))

    def __repr__(self):
        return "<Rating id=%d, Movie id=%d, User id=%d, Rating=%d >" %(self.id, self.movie_id, self.user_id, self.rating)

### End class declarations

def get_user(email, password):
    table_user = session.query(User).filter(User.email == email).first()

    if table_user.password == password:
        return table_user

    else:
        return False


def get_all_users():
    all_users = session.query(User).limit(10).all()
    return all_users


def get_movies_by_user(user_id):
    all_ratings = session.query(Rating).filter(Rating.user_id==user_id).all()
    all_movies = []
    for r in all_ratings:
        all_movies.append((r.movie, r.rating))
    return all_movies


def get_ratings_by_movie(movie_id):
    all_ratings = session.query(Rating).filter(Rating.movie_id==movie_id).all()
    return all_ratings


def get_rating_by_user(user_id, movie_id):
    rating = session.query(Rating).filter(Rating.user_id==user_id, Rating.movie_id==movie_id).first()
    return rating

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
