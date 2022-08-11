from flask import request
from flask_restx import (Resource,
                         Namespace)
from container import director_service
from blueprints.movie.dao.model.director import DirectorSchema

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        """
        Возвращает список режиссеров
        """
        directors = director_service.get_all()
        return directors_schema.dump(directors), 200

    def post(self):
        """
        Добавляет режиссера
        """
        director_service.create(director_schema.dump(request.json))
        return "", 201


@director_ns.route('/<int:did>/')
class DirectorView(Resource):
    def put(self, did: int):
        """
        Обновление режиссера
        """
        director_data = director_schema.load(request.json)
        director = director_service.update(did, director_data)
        if director:
            return "", 204
        return "", 404

    def delete(self, did: int):
        """
        Удаление режиссера
        """
        director = director_service.delete(did)
        if director:
            return "", 204
        return "", 404
