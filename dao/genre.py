# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД
from dao.model.genre import  Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_one(self, mid):
        return self.session.query(Genre).get(mid)

    # def delete(self, mid):
    #     movie = self.get_one(mid)
    #     self.session.delete(movie)
    #     self.session.commit()
    #
    # def update(self,data):
    #     mid = data.get("id")
    #     movie = self.get_one(mid)
    #     if "title" in data:
    #         movie.title = data.get("title")
    #     if "description" in data:
    #         movie.description = data.get("description")
    #     if "trailer" in data:
    #         movie.trailer = data.get("trailer")
    #     if "year" in data:
    #         movie.year = data.get("year")
    #     if "rating" in data:
    #         movie.rating = data.get("rating")
    #     self.session.commit()
    #     return movie
    #
    # def create(self, data):
    #     movie = Movie(**data)
    #     self.session.add(movie)
    #     self.session.commit()
    #     return movie
    #
