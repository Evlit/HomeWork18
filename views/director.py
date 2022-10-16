from flask_restx import Resource, Namespace
from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')
directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()


@director_ns.route('/')
class DirectorsView(Resource):
    """
    Класс режиссеров
    """
    def get(self):
        """
        Вывод всех режиссеров
        """
        return directors_schema.dump(director_service.get_all()), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    """
    Класс режиссер
    """
    def get(self, did):
        """
        Вывод режиссера по id
        """
        director = director_service.get_one(did)
        if not director:
            return f"Нет записи с таким номером {did}", 404
        return director_schema.dump(director)
