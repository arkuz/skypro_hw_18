import calendar
import datetime
import jwt

from blueprints.movie.services.user_service import UserService
from const import (JWT_SECRET,
                   JWT_ALGORITHM,
                   JWT_ACCESS_TOKEN_LIFE_TIME_MIN,
                   JWT_REFRESH_TOKEN_LIFE_TIME_DAY)
from flask import (request,
                   abort)


class AuthService:

    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def get_username(self) -> str:
        return request.json.get('username')

    def get_password(self) -> str:
        return request.json.get('password')

    def get_refresh_token(self) -> str:
        return request.json.get('refresh_token')

    def generate_access_token(self, data: dict) -> str:
        token_life_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=JWT_ACCESS_TOKEN_LIFE_TIME_MIN)
        data["exp"] = calendar.timegm(token_life_time.timetuple())
        return jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

    def generate_refresh_token(self, data: dict) -> str:
        token_life_time = datetime.datetime.utcnow() + datetime.timedelta(days=JWT_REFRESH_TOKEN_LIFE_TIME_DAY)
        data["exp"] = calendar.timegm(token_life_time.timetuple())
        return jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

    def check_token(self, token: str) -> bool:
        try:
            jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            return True
        except Exception:
            return False

    def generate_tokens(self, username: str, password: str | None, is_refresh=False) -> dict:
        user = self.user_service.get_by_username(username)

        if not user:
            raise abort(404)

        if not is_refresh:
            hash_password = self.user_service.get_password_hash(password)
            if not self.user_service.compare_passwords(hash_password, password):
                abort(400)

        data = {
            'username': username,
            'password': password,
            'role': user.role,
        }

        return {
            'access_token': self.generate_access_token(data),
            'refresh_token': self.generate_refresh_token(data),
        }

    def generate_tokens_by_refresh_token(self, token: str) -> dict:
        token_data = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        username = token_data.get('username')
        return self.generate_tokens(username, None, is_refresh=True)
