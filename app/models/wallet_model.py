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

    def __init__(
        self,
        name: str,
        stake_percent: float,
        stop_gain: float,
        stop_loss: float,
        initial_balance: float,
        current_balance: float,
        active_status: bool,
        notifications_settings: str,
    ):
        self.name = name
        self.stake_percent = stake_percent
        self.stop_gain = stop_gain
        self.stop_loss = stop_loss
        self.initial_balance = initial_balance
        self.current_balance = current_balance
        self.active_status = active_status
        self.notifications_settings = notifications_settings

    def __repr__(self) -> str:
        return f"Wallet({self.name}, {self.stake_percent}, {self.stop_gain}, \
            {self.stop_loss}, {self.initial_balance}, {self.current_balance}, \
            {self.active_status}, {self.notifications_settings})"
