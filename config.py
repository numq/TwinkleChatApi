import base64
import os

basedir = os.path.abspath(os.path.dirname(__file__))
main_db = os.path.join(basedir, 'db.sqlite')
test_db = os.path.join(basedir, 'test.sqlite')


class Config:
    DEBUG = True
    TESTING = True
    SECRET_KEY = base64.b64encode(os.urandom(64)).decode('utf-8')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {
        'db': 'sqlite:///' + os.path.join(basedir, main_db),
        'test': 'sqlite:///' + os.path.join(basedir, test_db)
    }


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, main_db)


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, test_db)
