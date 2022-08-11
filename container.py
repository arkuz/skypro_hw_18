from database import db
from blueprints.movie.dao.director_dao import DirectorDAO
from blueprints.movie.dao.genre_dao import GenreDAO
from blueprints.movie.dao.movie_dao import MovieDAO
from blueprints.movie.services.director_service import DirectorService
from blueprints.movie.services.genre_service import GenreService
from blueprints.movie.services.movie_service import MovieService

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)
