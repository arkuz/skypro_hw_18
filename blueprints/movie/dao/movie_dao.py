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

    def update(self, id: int, data: dict) -> Movie | None:
        movie = self.get_one(id)
        if movie:
            if "title" in data:
                movie.title = data.get("title")
            if "description" in data:
                movie.description = data.get("description")
            if "trailer" in data:
                movie.trailer = data.get("trailer")
            if "year" in data:
                movie.year = data.get("year")
            if "rating" in data:
                movie.rating = data.get("rating")
            if "genre_id" in data:
                movie.genre_id = data.get("genre_id")
            if "director_id" in data:
                movie.director_id = data.get("director_id")
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

    def get_movies_by_director(self, did) -> [Movie]:
        return Movie.query.filter(Movie.director_id == did).all()

    def get_movies_by_genre(self, gid) -> [Movie]:
        return Movie.query.filter(Movie.genre_id == gid).all()

    def get_movies_by_year(self, year) -> [Movie]:
        return Movie.query.filter(Movie.year == year).all()
