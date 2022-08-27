import base64
import hashlib
import hmac
from blueprints.movie.dao.user_dao import UserDAO
from blueprints.movie.dao.model.user import User
from blueprints.movie.services.base_service import BaseService
from const import (PWD_ALGORITHM,
                   PWD_HASH_SALT,
                   PWD_HASH_ITERATIONS)


class UserService(BaseService):

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, id: int) -> User | None:
        return self.dao.get_one(id)

    def get_all(self) -> [User]:
        return self.dao.get_all()

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def create(self, data: dict) -> User:
        password = data['password']
        data['password'] = self.get_password_hash(password)
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

    def get_password_hash(self, password: str) -> str:
        return base64.b64encode(
            hashlib.pbkdf2_hmac(
                PWD_ALGORITHM,
                password.encode('utf-8'),
                PWD_HASH_SALT,
                PWD_HASH_ITERATIONS,
            )).decode('utf-8')

    def compare_passwords(self, password_hash, other_password) -> bool:
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac(
                PWD_ALGORITHM,
                other_password.encode(),
                PWD_HASH_SALT,
                PWD_HASH_ITERATIONS)
        )
