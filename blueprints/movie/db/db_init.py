import os
from app import db, create_app
from const import BASE_DIR
from utils import _load_json_file
from blueprints.movie.models.movie import (Movie,
                                           Director,
                                           Genre)
from config import read_env

FIXTURES_DIR = os.path.join(BASE_DIR, 'blueprints', 'movie', 'db', 'fixtures')
DUMP_DIR = os.path.join(FIXTURES_DIR, 'dump.json')


def load_dump() -> list[dict]:
    return _load_json_file(DUMP_DIR)


def add_movies() -> None:
    movies = load_dump()['movies']
    prepared_movies = [Movie(**movie) for movie in movies]
    db.session.add_all(prepared_movies)
    db.session.commit()


def add_directors() -> None:
    directors = load_dump()['directors']
    prepared_directors = [Director(**director) for director in directors]
    db.session.add_all(prepared_directors)
    db.session.commit()


def add_genres() -> None:
    genres = load_dump()['genres']
    prepared_genres = [Genre(**genre) for genre in genres]
    db.session.add_all(prepared_genres)
    db.session.commit()


def init_db() -> None:
    config = read_env()
    app = create_app(config)
    with app.app_context():
        db.drop_all()
        db.create_all()
        add_movies()
        add_directors()
        add_genres()


if __name__ == '__main__':
    init_db()
    print('Database initialized successfully')
