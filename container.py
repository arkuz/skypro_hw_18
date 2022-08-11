from blueprints.movie.dao.director_dao import DirectorDAO
from blueprints.movie.dao.genre_dao import GenreDAO
from blueprints.movie.dao.movie_dao import MovieDAO
from database import db

director_dao = DirectorDAO(db.session)
genre_dao = GenreDAO(db.session)
movie_dao = MovieDAO(db.session)
