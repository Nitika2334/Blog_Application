import os

class Config:
    SECRET_KEY = 'mysecret'
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/mini_blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
