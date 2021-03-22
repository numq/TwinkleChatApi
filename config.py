import base64
import os

from app.utilities import constants

basedir = constants.DATABASE_PACKAGE
main_db = os.path.join(basedir, 'db.sqlite')
test_db = os.path.join(basedir, 'test.sqlite')


class Config:
    DEBUG = True
    TESTING = True
    SECRET_KEY = base64.b64encode(os.urandom(64)).decode('utf-8')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {
        'db': 'sqlite:///' + main_db,
        'test': 'sqlite:///' + test_db
    }


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + main_db


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + test_db
