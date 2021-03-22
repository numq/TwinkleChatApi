from app import create_app
from config import ProductionConfig

# Init
app = create_app(ProductionConfig)
app.url_map.strict_slashes = False


@app.route('/', methods=['GET'])
def get_user():
    return 'index'


if __name__ == "__main__":
    from database.models import db

    db.init_app(app)
    db.app = app
    app.run()
