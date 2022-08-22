from blueprints.movie.dao.user_dao import UserDAO
from blueprints.movie.dao.model.user import User
from blueprints.movie.services.base_service import BaseService


class UserService(BaseService):

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, id: int) -> User | None:
        return self.dao.get_one(id)

    def get_all(self) -> [User]:
        return self.dao.get_all()

    def create(self, data: dict) -> User:
        return self.dao.create(data)

    def update(self, id: int, data: dict) -> User | None:
        user = self.get_one(id)
        if user:
            if "username" in data:
                user.username = data.get("username")
            if "password" in data:
                user.password = data.get("password")
            if "role" in data:
                user.role = data.get("role")
            self.dao.update(user)
            return user
        return None

    def delete(self, id: int) -> User | None:
        return self.dao.delete(id)
