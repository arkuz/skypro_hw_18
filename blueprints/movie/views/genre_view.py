from flask import request
from flask_restx import (Resource,
                         Namespace)
from container import genre_service
from blueprints.movie.dao.model.genre import GenreSchema

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        """
        Возвращает список жанров
        """
        genres = genre_service.get_all()
        return genres_schema.dump(genres), 200

    def post(self):
        """
        Добавляет жанр
        """
        genre_service.create(genre_schema.dump(request.json))
        return "", 201


@genre_ns.route('/<int:gid>/')
class GenreView(Resource):
    def put(self, gid: int):
        """
        Обновление жанра
        """
        genre_data = genre_schema.load(request.json)
        genre = genre_service.update(gid, genre_data)
        if genre:
            return "", 204
        return "", 404

    def delete(self, gid: int):
        """
        Удаление жанра
        """
        genre = genre_service.delete(gid)
        if genre:
            return "", 204
        return "", 404
