from blueprints.movie.dao.base_dao import BaseDAO
from blueprints.movie.dao.model.genre import Genre


class GenreDAO(BaseDAO):

    def __init__(self, session):
        self.session = session

    def get_one(self, id: int) -> Genre | None:
        return self.session.query(Genre).get(id)

    def get_all(self) -> [Genre]:
        return self.session.query(Genre).all()

    def create(self, data: dict) -> Genre:
        genre = Genre(**data)
        self.session.add(genre)
        self.session.commit()
        return genre

    def update(self, genre: Genre) -> Genre | None:
        if genre:
            self.session.add(genre)
            self.session.commit()
            return genre
        return None

    def delete(self, id: int) -> Genre | None:
        genre = self.get_one(id)
        if genre:
            self.session.delete(genre)
            self.session.commit()
            return genre
        return None
