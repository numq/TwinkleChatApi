from flask import Flask

from config import TestConfig


def create_app(config=TestConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    return app


def register_blueprints(app):
    from app.blueprints.user import bp_user

    # Blueprints
    app.register_blueprint(bp_user)
