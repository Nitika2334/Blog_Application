import os

class Config:
    SECRET_KEY = 'mysecret'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:1234@localhost:5432/mini_blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
