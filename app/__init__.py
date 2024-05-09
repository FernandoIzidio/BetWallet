from flask import Flask
from .config import SECRET_KEY
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///wallet.db"

    from .routes import app as app_bp
    from models import user_model

    app.register_blueprint(app_bp)

    db = SQLAlchemy(app)
    db.create_all()

    return app
