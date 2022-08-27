import logging
import os.path
import const
from typing import Type
from flask import Flask
from blueprints.movie.views.director_view import director_ns
from blueprints.movie.views.genre_view import genre_ns
from blueprints.movie.views.movie_view import movie_ns
from blueprints.movie.views.user_view import user_ns
from blueprints.movie.views.auth_view import auth_ns
from database import db
from blueprints.movie import (movie_blueprint,
                              api)
from config import BaseConfig

logging.basicConfig(filename=os.path.join(const.BASE_DIR, 'log', 'log.log'),
                    level=logging.INFO,
                    format='%(asctime)s - [%(levelname)s] - %(name)s -'
                           ' (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')  # noqa
logger = logging.getLogger(__name__)


def create_app(config: Type[BaseConfig]) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()

    app.register_blueprint(movie_blueprint)

    db.init_app(app)

    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    api.init_app(app)

    return app
