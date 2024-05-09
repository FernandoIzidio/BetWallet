from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone_number = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    id_balance = db.Column(
        db.Integer, db.ForeignKey("balance.id"), unique=True, nullable=False
    )

    def __init__(self, name, email, phone_number, password, id_balance):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.id_balance = id_balance

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.phone_number}', \
            '{self.password}', '{self.id_balance}')"
