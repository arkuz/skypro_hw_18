import logging
import os.path
from typing import Type
import const
from flask import Flask
from blueprints.movie.models.movie import db
from blueprints.movie.views import movie_blueprint, api
from config import BaseConfig

logging.basicConfig(filename=os.path.join(const.BASE_DIR, 'log', 'log.log'),
                    level=logging.INFO,
                    format='%(asctime)s - [%(levelname)s] - %(name)s -'
                           ' (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')
logger = logging.getLogger(__name__)


def create_app(config: Type[BaseConfig]) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(movie_blueprint)

    db.init_app(app)
    api.init_app(app)

    return app
