import pytest

""" 
run with: 

python -m pytest tests

"""


@pytest.fixture
def test_app():
    from app import create_app
    from config import TestConfig
    from app.extensions import db as _db

    app = create_app(TestConfig)
    _db.init_app(app)
    _db.app = app
    _db.create_all()
    return app
