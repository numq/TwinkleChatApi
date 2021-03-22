from app import create_app
from app.extensions import db
from config import ProductionConfig

# Init
app = create_app(ProductionConfig)
app.url_map.strict_slashes = False


@app.route('/', methods=['GET'])
def get_user():
    return 'index'


if __name__ == "__main__":
    db.init_app(app)
    app.run()
