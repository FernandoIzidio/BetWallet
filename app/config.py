from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
import os


load_dotenv()
SECRET_KEY = generate_password_hash(os.getenv("SECRET_KEY"))
BETTING_POINT = "https://api.betfair.com/exchange/betting/rest/v1.0/"
ACCOUNT_POINT = "https://api.betfair.com/exchange/account/rest/v1.0/"

header = {
    "X-Application": os.getenv("APP_KEY"),
    "X-Authentication": os.getenv("SESSION_KEY"),
    "content-type": "application/json",
}


# https://docs.developer.betfair.com/display/1smk3cen4v3lu3yomq5qye0ni/Betting+Type+Definitions#BettingTypeDefinitions-MarketFilter

json_req = {
    "filter": {},
}
