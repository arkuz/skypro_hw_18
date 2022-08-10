from flask_sqlalchemy import SQLAlchemy

from blueprints.movie.dao.director_dao import DirectorDAO

db = SQLAlchemy()

director_dao = DirectorDAO(db.session)
