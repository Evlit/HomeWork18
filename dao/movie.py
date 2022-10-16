# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД
from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_by_director(self, did):
        return self.session.query(Movie).filter(Movie.director_id == did).all()

    def get_by_genre(self, gid):
        return self.session.query(Movie).filter(Movie.genre_id == gid).all()

    def get_by_year(self, yid):
        return self.session.query(Movie).filter(Movie.year == yid).all()

    def delete(self, movie):
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie):
        # self.session.add(movie)
        self.session.commit()
        return movie

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

