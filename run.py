from app import create_app
from config import read_env

config = read_env()

app = create_app(config=config)
