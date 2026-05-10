from flask import Flask
from app.models.db import db, migrate
from app.config import Config
from app.controllers.registro import registro

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(registro, url_prefix="/registro")

    return app