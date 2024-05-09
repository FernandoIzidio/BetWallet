from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
import os

load_dotenv()
SECRET_KEY = generate_password_hash(os.getenv("SECRET_KEY"))
