from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
import os


load_dotenv()
SECRET_KEY = generate_password_hash(os.getenv("SECRET_KEY"))
BETTING_POINT = "https://api.betfair.com/exchange/betting/rest/v1.0/"
ACCOUNT_POINT = "https://api.betfair.com/exchange/account/rest/v1.0"

header = {
    "X-Application": os.getenv("APP_KEY"),
    "X-Authentication": os.getenv("SESSION_TOKEN"),
    "content-type": "application/json",
}

json_req = '{"filter":{ }}'
