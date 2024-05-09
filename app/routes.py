from flask import Blueprint

app = Blueprint("routes", __name__)


@app.route("/")
def index():
    return "Olá, mundo!"
