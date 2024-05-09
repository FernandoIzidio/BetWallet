from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Balance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    money = db.Column(db.Integer, nullable=False)
