from flask import (Blueprint,
                   request)
from flask_restx import (Api,
                         Resource)
from container import (director_service,
                       genre_service,
                       movie_service)

from blueprints.movie.dao.model.director import DirectorSchema
from blueprints.movie.dao.model.genre import GenreSchema
from blueprints.movie.dao.model.movie import MovieSchema

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

movie_blueprint = Blueprint('movie_blueprint', __name__)

api = Api()

movie_ns = api.namespace('movies')
genre_ns = api.namespace('genres')
director_ns = api.namespace('directors')


@movie_ns.route('/')
class MoviesView(Resource):

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

    def post(self):
        """
        Добавляет фильм
        """
        movie_service.create(movie_schema.dump(request.json))
        return "", 201


@movie_ns.route('/<int:mid>/')
class MovieView(Resource):

    def get(self, mid: int):
        """
        Возвращает фильм по id
        """
        movie = movie_service.get_one(mid)
        if movie:
            return movie_schema.dump(movie), 200
        return "", 404

    def put(self, mid: int):
        """
        Обновление фильма
        """
        movie_data = movie_schema.load(request.json)
        movie = movie_service.update(mid, movie_data)
        if movie:
            return "", 204
        return "", 404

    def delete(self, mid: int):
        """
        Удаление фильма
        """
        movie = movie_service.delete(mid)
        if movie:
            return "", 204
        return "", 404


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
