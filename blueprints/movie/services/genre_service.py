from blueprints.movie.dao.genre_dao import GenreDAO
from blueprints.movie.dao.model.genre import Genre
from blueprints.movie.services.base_service import BaseService


class GenreService(BaseService):

    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, id: int) -> Genre | None:
        return self.dao.get_one(id)

    def get_all(self) -> [Genre]:
        return self.dao.get_all()

    def create(self, data: dict) -> Genre:
        return self.dao.create(data)

    def update(self, id: int, data: dict) -> Genre | None:
        genre = self.get_one(id)
        if genre:
            if "name" in data:
                genre.name = data.get("name")
                self.dao.update(genre)
                return genre
        return None

    def delete(self, id: int) -> Genre | None:
        return self.dao.delete(id)
