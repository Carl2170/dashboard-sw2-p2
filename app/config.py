import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:Eyeoftiger123@localhost:5432/dashboard")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
