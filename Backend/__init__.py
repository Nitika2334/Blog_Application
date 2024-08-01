from flask import Flask,register_blueprint
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from Controllers.authController import auth_controller

    register_blueprint(auth_controller, url_prefix='/api')

    from Views.authView import auth_views

    register_blueprint(auth_views)

    return app
