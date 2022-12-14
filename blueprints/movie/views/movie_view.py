from flask import request, url_for
from flask_restx import (Resource,
                         Namespace)
from container import movie_service
from blueprints.movie.dao.model.movie import MovieSchema
from helpers.auth_helper import (auth_required,
                                 admin_required)

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):

    @auth_required
    def get(self):
        """
        Возвращает список всех фильмов.
        Возвращает фильмы по id режиссера или id жанра или по году
        """
        did = request.args.get('director_id')
        if did:
            movies = movie_service.get_movies_by_director(did)
            return movies_schema.dump(movies), 200

        gid = request.args.get('genre_id')
        if gid:
            movies = movie_service.get_movies_by_genre(gid)
            return movies_schema.dump(movies), 200

        year = request.args.get('year')
        if year:
            movies = movie_service.get_movies_by_year(year)
            return movies_schema.dump(movies), 200

        movies = movie_service.get_all()

        return movies_schema.dump(movies), 200

    @admin_required
    def post(self):
        """
        Добавляет фильм
        """
        movie = movie_service.create(movie_schema.dump(request.json))
        return "", 201, {
            'Location': f"{url_for('movies_movies_view')}{movie.id}"}


@movie_ns.route('/<int:mid>/')
class MovieView(Resource):

    @auth_required
    def get(self, mid: int):
        """
        Возвращает фильм по id
        """
        movie = movie_service.get_one(mid)
        if movie:
            return movie_schema.dump(movie), 200
        return "", 404

    @admin_required
    def put(self, mid: int):
        """
        Обновление фильма
        """
        movie_data = movie_schema.load(request.json)
        movie = movie_service.update(mid, movie_data)
        if movie:
            return "", 204
        return "", 404

    @admin_required
    def delete(self, mid: int):
        """
        Удаление фильма
        """
        movie = movie_service.delete(mid)
        if movie:
            return "", 204
        return "", 404
