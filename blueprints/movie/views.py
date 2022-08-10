import logging
from flask import (Blueprint,
                   request)
from flask_restx import (Api,
                         Resource)

import const
from blueprints.movie.models.movie import (Movie,
                                           Director,
                                           Genre)
from blueprints.movie.schemes.movie import (movie_schema,
                                            movies_schema,
                                            director_schema,
                                            directors_schema,
                                            genre_schema,
                                            genres_schema)
from blueprints.movie.models.movie import db

logger = logging.getLogger(__name__)
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
        Возвращает фильмы по id режиссера и по id жанра.
        Возвращает только фильмы с определенным режиссером и жанром по их id
        """
        req_director = request.args.get('director_id')
        req_genre = request.args.get('genre_id')
        page = request.args.get('page', type=int, default=1)
        if req_director and req_genre:
            movies = Movie.query.filter(
                Movie.director_id == req_director,
                Movie.genre_id == req_genre).all()
            return movies_schema.dump(movies), 200
        if req_director:
            movies = Movie.query.filter(
                Movie.director_id == req_director).all()
            return movies_schema.dump(movies), 200
        if req_genre:
            movies = db.session.query(Movie).filter(
                Movie.genre_id == req_genre).all()
            return movies_schema.dump(movies)
        movies = db.session.query(Movie).paginate(
            page, const.MOVIES_PER_PAGE, False).items
        return movies_schema.dump(movies), 200

    def post(self):
        """
        Добавляет фильм
        """
        movie = Movie(**movie_schema.load(request.json))
        db.session.add(movie)
        db.session.commit()
        return "", 201


@movie_ns.route('/<int:mid>/')
class MovieView(Resource):

    def get(self, mid: int):
        """
        Возвращает фильм по id
        """
        movie = db.session.query(Movie).get(mid)
        if movie:
            return movie_schema.dump(movie), 200
        return "", 404

    def put(self, mid: int):
        """
        Обновление фильма
        """
        movie = Movie.query.get(mid)
        if movie:
            req_json = request.json
            if "title" in req_json:
                movie.title = req_json.get("title")
            if "description" in req_json:
                movie.description = req_json.get("description")
            if "trailer" in req_json:
                movie.trailer = req_json.get("trailer")
            if "year" in req_json:
                movie.year = req_json.get("year")
            if "rating" in req_json:
                movie.rating = req_json.get("rating")
            if "genre_id" in req_json:
                movie.genre_id = req_json.get("genre_id")
            if "director_id" in req_json:
                movie.director_id = req_json.get("director_id")
                db.session.add(movie)
                db.session.commit()
                return "", 204

        return "", 404

    def delete(self, mid: int):
        """
        Удаление фильма
        """
        movie = Movie.query.get(mid)
        if movie:
            db.session.delete(movie)
            db.session.commit()
            return "", 204
        return "", 404


@director_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        """
        Возвращает список режиссеров
        """
        directors = Director.query.all()
        return directors_schema.dump(directors), 200

    def post(self):
        """
        Добавляет режиссера
        """
        director = Director(**director_schema.load(request.json))
        db.session.add(director)
        db.session.commit()
        return "", 201


@director_ns.route('/<int:did>/')
class DirectorView(Resource):
    def put(self, did: int):
        """
        Обновление режиссера
        """
        director = Director.query.get(did)
        if director:
            req_json = request.json
            if "name" in req_json:
                director.director_id = req_json.get("name")
                db.session.add(director)
                db.session.commit()
                return "", 204
        return "", 404

    def delete(self, did: int):
        """
        Удаление режиссера
        """
        director = Director.query.get(did)
        if director:
            db.session.delete(director)
            db.session.commit()
            return "", 204
        return "", 404


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        """
        Возвращает список жанров
        """
        genres = db.session.query(Genre).all()
        return genres_schema.dump(genres), 200

    def post(self):
        """
        Добавляет жанр
        """
        genre = Genre(**genre_schema.load(request.json))
        with db.session.begin():
            db.session.add(genre)
        return "", 201


@genre_ns.route('/<int:gid>/')
class GenreView(Resource):
    def put(self, gid: int):
        """
        Обновление жанра
        """
        genre = Genre.query.get(gid)
        if genre:
            req_json = request.json
            if "name" in req_json:
                genre.name = req_json.get("name")
                db.session.add(genre)
                db.session.commit()
                return "", 204
            return "", 404

    def delete(self, gid: int):
        """
        Удаление жанра
        """
        genre = Genre.query.get(gid)
        if genre:
            db.session.delete(genre)
            db.session.commit()
            return "", 204
        return "", 404
