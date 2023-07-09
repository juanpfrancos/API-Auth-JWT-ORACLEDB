from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

CS = os.getenv("cs")
DB_USER = os.getenv("db_user")
DB_PASS = os.getenv("db_pass")
DB_TABLE = os.getenv("db_table")
SECRET_KEY = os.getenv("secret_key")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")