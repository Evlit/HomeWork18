from flask import request
from flask_restx import Resource, Namespace
from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')
movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@movie_ns.route('/')
class MoviesView(Resource):
    """
    Класс фильмов
    """

    def get(self):
        """
        Обработка запросов Get
        получение всего списка фильмов
        """
        key_dir = int(request.args.get('director_id', 0))
        key_genre = int(request.args.get('genre_id', 0))
        key_year = int(request.args.get('year', 0))
        if key_dir + key_genre + key_year == 0:
            return movies_schema.dump(movie_service.get_all()), 200
        elif key_dir > 0 and key_year == 0 and key_genre == 0:
            result = movie_service.get_by_director(key_dir)
            if len(result) > 0:
                return movies_schema.dump(result), 200
            else:
                return "В базе нет записей с таким номером"
        elif key_dir == 0 and key_year == 0 and key_genre > 0:
            result = movie_service.get_by_genre(key_genre)
            if len(result) > 0:
                return movies_schema.dump(result), 200
            else:
                return "В базе нет записей с таким номером"
        elif key_dir == 0 and key_year > 0 and key_genre == 0:
            result = movie_service.get_by_year(key_year)
            if len(result) > 0:
                return movies_schema.dump(result), 200
            else:
                return "В базе нет записей с таким номером"

    def post(self):
        """
        Обработка POST - добавление фильма
        """
        data = request.json
        movie_service.create(data)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    """
    Класс фильма по id
    """

    def get(self, mid):
        """
        Вывод фильма по id
        """
        try:
            result = movie_service.get_one(mid)
            return movie_schema.dump(result), 200
        except Exception as e:
            return f"Нет записи с таким номером {e}"

    def put(self, mid: int):
        """
        Обработка запроса PUT
        """
        movie = movie_service.get_one(mid)
        if not movie:
            return f"Нет записи с таким номером {mid}", 404
        data = request.json
        data["id"] = mid
        movie_service.update(data)
        return "", 204

    def patch(self, mid: int):
        """
        Обработка запроса PATCH
        """
        movie = movie_service.get_one(mid)
        if not movie:
            return f"Нет записи с таким номером {mid}", 404
        data = request.json
        data["id"] = mid
        movie_service.update(data)
        return "", 204

    def delete(self, mid: int):
        """
        Обработка запроса DELETE
        """
        movie = movie_service.get_one(mid)
        if not movie:
            return f"Нет записи с таким номером {mid}", 404
        movie_service.delete(mid)
        return "", 204
