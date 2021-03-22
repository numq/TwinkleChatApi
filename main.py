from flask_sqlalchemy import SQLAlchemy

from app import create_app, register_blueprints
from config import ProductionConfig

# Init
app = create_app(ProductionConfig)
app.url_map.strict_slashes = False


@app.route('/', methods=['GET'])
def get_user():
    return 'index'


# Init db
db = SQLAlchemy(app)

if __name__ == "__main__":
    register_blueprints(app)
    db.init_app(app)
    app.run()
