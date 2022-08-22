from flask import request, url_for
from flask_restx import (Resource,
                         Namespace)
from container import user_service
from blueprints.movie.dao.model.user import UserSchema

user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Подготавливаем список колонок для схемы без отображения поля password
user_schema_columns = user_schema.declared_fields.keys()
user_columns = tuple(col for col in user_schema_columns if col != 'password')

user_schema_column_only = UserSchema(only=user_columns)
users_schema_column_only = UserSchema(many=True, only=user_columns)

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):

    def get(self):
        """
        Возвращает список пользователей
        """
        users = user_service.get_all()
        return users_schema_column_only.dump(users), 200

    def post(self):
        """
        Добавляет пользователя
        """
        user = user_service.create(user_schema.dump(request.json))
        return "", 201, {
            'Location': f"{url_for('users_users_view')}{user.id}"}


@user_ns.route('/<int:did>/')
class UserView(Resource):

    def get(self, did: int):
        """
        Возвращает пользователя по id
        """
        user = user_service.get_one(did)
        return user_schema_column_only.dump(user), 200

    def put(self, did: int):
        """
        Обновление пользователя
        """
        user_data = user_schema.load(request.json)
        user = user_service.update(did, user_data)
        if user:
            return "", 204
        return "", 404

    def delete(self, did: int):
        """
        Удаление пользователя
        """
        user = user_service.delete(did)
        if user:
            return "", 204
        return "", 404
