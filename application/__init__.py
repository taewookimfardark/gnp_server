from flask import Flask
from config import Config
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app = Config.init_app(app)
    db.init_app(app)

    from api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")
    return app

app = create_app()


if __name__ == "__main__":
    app.run()