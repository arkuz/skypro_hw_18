import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

PWD_ALGORITHM = 'sha256'
PWD_HASH_SALT = b'write_your_salt'
PWD_HASH_ITERATIONS = 100_000

JWT_SECRET = 'write_your_secret'
JWT_ALGORITHM = 'HS256'
JWT_ACCESS_TOKEN_LIFE_TIME_MIN = 30
JWT_REFRESH_TOKEN_LIFE_TIME_DAY = 30
