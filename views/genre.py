# Представление для жанров
from flask_restx import Resource, Namespace
from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')
genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


@genre_ns.route('/')
class GenresView(Resource):
    """
    Класс жанров
    """
    def get(self):
        """
        Вывод всех жанров
        """
        return genres_schema.dump(genre_service.get_all()), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    """
    Класс жанра
    """
    def get(self, gid):
        """
        Вывод жанра по id
        """
        genre = genre_service.get_one(gid)
        if not genre:
            return f"Нет записи с таким номером {gid}", 404
        return genre_schema.dump(genre)
