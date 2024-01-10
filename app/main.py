import os

from blueprints.v1.avaaz import blueprint as avaaz_blueprint_v1
from flask import Flask
from models.base import db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI", "sqlite:///:memory:")  # fmt: skip
    app.register_blueprint(avaaz_blueprint_v1, url_prefix="/v1")

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app


app = create_app()
