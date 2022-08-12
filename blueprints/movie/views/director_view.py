from flask import request, url_for
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
        director = director_service.create(director_schema.dump(request.json))
        return "", 201, {
            'Location': f"{url_for('directors_directors_view')}{director.id}"}


@director_ns.route('/<int:did>/')
class DirectorView(Resource):

    def get(self, did: int):
        """
        Возвращает режиссера по id
        """
        director = director_service.get_one(did)
        return director_schema.dump(director), 200

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
