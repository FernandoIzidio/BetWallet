from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    stake_percent = db.Column(db.Float, nullable=False)
    stop_gain = db.Column(db.Float, nullable=False)
    stop_loss = db.Column(db.Float, nullable=False)

    initial_balance = db.Column(db.Float, nullable=False)

    current_balance = db.Column(db.Float, nullable=False)

    transaction_history = db.relationship("Transaction", backref="wallet", lazy=True)

    date_created = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.now(),
    )

    last_updated = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.now(),
        onupdate=datetime.now(),
    )

    active_status = db.Column(db.Boolean, nullable=False, default=True)
    notifications_settings = db.Column(db.JSON, nullable=True)

    id_balance = db.Column(db.Integer, db.ForeignKey("balance.id"))
