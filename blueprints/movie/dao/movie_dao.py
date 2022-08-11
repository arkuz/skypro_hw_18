from blueprints.movie.dao.base_dao import BaseDAO
from blueprints.movie.dao.model.movie import Movie


class MovieDAO(BaseDAO):

    def __init__(self, session):
        self.session = session

    def get_one(self, id: int) -> Movie | None:
        return self.session.query(Movie).get(id)

    def get_all(self) -> [Movie]:
        return self.session.query(Movie).all()

    def create(self, data: dict) -> Movie:
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, movie: Movie) -> Movie | None:
        if movie:
            self.session.add(movie)
            self.session.commit()
            return movie
        return None

    def delete(self, id: int) -> Movie | None:
        movie = self.get_one(id)
        if movie:
            self.session.delete(movie)
            self.session.commit()
            return movie
        return None

    def get_movies_by_director(self, did: int) -> [Movie]:
        return Movie.query.filter(Movie.director_id == did).all()

    def get_movies_by_genre(self, gid: int) -> [Movie]:
        return Movie.query.filter(Movie.genre_id == gid).all()

    def get_movies_by_year(self, year: int) -> [Movie]:
        return Movie.query.filter(Movie.year == year).all()
