from blueprints.movie.dao.base_dao import BaseDAO
from blueprints.movie.dao.model.director import Director


class DirectorDAO(BaseDAO):

    def __init__(self, session):
        self.session = session

    def get_one(self, id: int) -> Director | None:
        return self.session.query(Director).get(id)

    def get_all(self) -> [Director]:
        return self.session.query(Director).all()

    def create(self, data: dict) -> Director:
        director = Director(**data)
        self.session.add(director)
        self.session.commit()
        return director

    def update(self, id: int, data: dict) -> Director | None:
        director = self.get_one(id)
        if director:
            if "name" in data:
                director.name = data.get("name")
                self.session.add(director)
                self.session.commit()
                return director
        return None

    def delete(self, id: int) -> Director | None:
        director = self.get_one(id)
        if director:
            self.session.delete(director)
            self.session.commit()
            return director
        return None
