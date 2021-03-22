from flask import Flask

from app.extensions import db
from config import TestConfig


def create_app(config=TestConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    app.url_map.strict_slashes = False
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    from app.extensions import db, ma
    db.init_app(app)
    ma.init_app(app)
    return None


def register_blueprints(app):
    from app.blueprints.user import bp_user
    app.register_blueprint(bp_user)
    return None
