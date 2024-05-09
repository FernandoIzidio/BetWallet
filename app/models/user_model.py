from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone_number = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    id_balance = db.Column(
        db.Integer,
        db.ForeignKey("balance.id"),
        unique=True,
    )
