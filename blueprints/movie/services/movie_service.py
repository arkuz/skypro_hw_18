from blueprints.movie.dao.movie_dao import MovieDAO
from blueprints.movie.dao.model.movie import Movie
from blueprints.movie.services.base_service import BaseService


class MovieService(BaseService):

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, id: int) -> Movie | None:
        return self.dao.get_one(id)

    def get_all(self) -> [Movie]:
        return self.dao.get_all()

    def create(self, data: dict) -> Movie:
        return self.dao.create(data)

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
                self.dao.update(movie)
            return movie
        return None

    def delete(self, id: int) -> Movie | None:
        return self.dao.delete(id)

    def get_movies_by_director(self, did: int) -> [Movie]:
        return self.dao.get_movies_by_director(did)

    def get_movies_by_genre(self, gid: int) -> [Movie]:
        return self.dao.get_movies_by_genre(gid)

    def get_movies_by_year(self, year: int) -> [Movie]:
        return self.dao.get_movies_by_year(year)
