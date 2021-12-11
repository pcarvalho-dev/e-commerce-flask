import datetime
import os

try:
    APP_ENV = str(os.environ['APP_ENV'])
except KeyError:
    APP_ENV = 'development'

ROOT = os.path.dirname(os.path.abspath(__file__))


class Config:
    # api
    API_VERSION = "v1"

    # sqlalchemy connect
    DB_NAME = os.environ.get('DB_NAME', 'marketplace_db')
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASS = os.environ.get('DB_PASS', 'root')
    DB_HOST = os.environ.get('DB_HOST', 'database')
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}?charset=utf8mb4'
    SQLALCHEMY_BINDS = {
        'slave': SQLALCHEMY_DATABASE_URI
    }

    # jwt
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY',
                                    'ZWNvbW1lcmNlQHNlY3JldF9rZXk=')
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRES = 3600
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(seconds=JWT_EXPIRES)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
