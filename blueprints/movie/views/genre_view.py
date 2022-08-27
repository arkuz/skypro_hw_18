from flask import request, url_for
from flask_restx import (Resource,
                         Namespace)
from container import genre_service
from blueprints.movie.dao.model.genre import GenreSchema
from helpers.auth_helper import (auth_required,
                                 admin_required)

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):

    @auth_required
    def get(self):
        """
        Возвращает список жанров
        """
        genres = genre_service.get_all()
        return genres_schema.dump(genres), 200

    @admin_required
    def post(self):
        """
        Добавляет жанр
        """
        genre = genre_service.create(genre_schema.dump(request.json))
        return "", 201, {
            'Location': f"{url_for('genres_genres_view')}{genre.id}"}


@genre_ns.route('/<int:gid>/')
class GenreView(Resource):

    @auth_required
    def get(self, gid: int):
        """
        Возвращает жанр по id
        """
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre), 200

    @admin_required
    def put(self, gid: int):
        """
        Обновление жанра
        """
        genre_data = genre_schema.load(request.json)
        genre = genre_service.update(gid, genre_data)
        if genre:
            return "", 204
        return "", 404

    @admin_required
    def delete(self, gid: int):
        """
        Удаление жанра
        """
        genre = genre_service.delete(gid)
        if genre:
            return "", 204
        return "", 404
