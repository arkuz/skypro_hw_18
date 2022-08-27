from blueprints.movie.dao.base_dao import BaseDAO
from blueprints.movie.dao.model.user import User


class UserDAO(BaseDAO):

    def __init__(self, session):
        self.session = session

    def get_one(self, id: int) -> User | None:
        return self.session.query(User).get(id)

    def get_all(self) -> [User]:
        return self.session.query(User).all()

    def get_by_username(self, username):
        return self.session.query(User).filter(User.username == username).first()

    def create(self, data: dict) -> User:
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, user: User) -> User | None:
        if user:
            self.session.add(user)
            self.session.commit()
            return user
        return None

    def delete(self, id: int) -> User | None:
        user = self.get_one(id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return user
        return None
