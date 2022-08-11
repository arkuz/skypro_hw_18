from blueprints.movie.dao.director_dao import DirectorDAO
from blueprints.movie.dao.model.director import Director
from blueprints.movie.services.base_service import BaseService


class DirectorService(BaseService):

    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, id: int) -> Director | None:
        return self.dao.get_one(id)

    def get_all(self) -> [Director]:
        return self.dao.get_all()

    def create(self, data: dict) -> Director:
        return self.dao.create(data)

    def update(self, id: int, data: dict) -> Director | None:
        director = self.get_one(id)
        if director:
            if "name" in data:
                director.name = data.get("name")
                self.dao.update(director)
                return director
        return None

    def delete(self, id: int) -> Director | None:
        return self.dao.delete(id)
