from flask import Blueprint
from flask_restx import Api

movie_blueprint = Blueprint('movie_blueprint', __name__)

api = Api()
