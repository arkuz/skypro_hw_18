from flask_restx import (Resource,
                         Namespace)
from container import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):

    def post(self):
        """
        Генерирует токены по логину и паролю
        """
        return auth_service.generate_tokens(auth_service.get_username(),
                                            auth_service.get_password()), 200

    def put(self):
        """
        Обновление access и refresh токенов по refresh токену
        """
        refresh_token = auth_service.get_refresh_token()
        return auth_service.generate_tokens_by_refresh_token(refresh_token), 200
