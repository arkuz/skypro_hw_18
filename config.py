import os
from typing import Type


class BaseConfig:
    JSON_AS_ASCII = False
    RESTX_JSON = {'ensure_ascii': False}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    DEBUG = False
    JSON_SORT_KEYS = True


class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movie.db'
    SQLALCHEMY_ECHO = True
    DEBUG = True


class ProdConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movie.db'


def read_env() -> Type[BaseConfig]:
    match os.getenv('FLASK_ENV'):
        case 'development':
            return DevConfig
        case 'production':
            return ProdConfig
        case _:
            raise EnvironmentError('FLASK_ENV does not set')
