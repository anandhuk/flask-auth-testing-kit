import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default_secret")
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI", "postgresql://myuser:mypassword@localhost:5432/auth_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "supersecretkey")