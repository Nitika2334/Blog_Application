from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from app.config import Config
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    from app.Models.UserModel import User
    from app.Models.CommentModel import Comment
    from app.Models.PostModel import Post

    from app.Controllers.authController import auth_controller
    # from app.Controllers.postController import post_controller
    # from app.Controllers.commentController import comment_controller

    with app.app_context():
        db.create_all() 

    app.register_blueprint(auth_controller, url_prefix='/api')
    # app.register_blueprint(post_controller, url_prefix='/api')
    # app.register_blueprint(comment_controller, url_prefix='/api')

    from app.Views.authView import auth_views
    # from app.Views.postView import post_views
    # from app.Views.commentView import comment_views

    app.register_blueprint(auth_views)
    # app.register_blueprint(post_views)
    # app.register_blueprint(comment_views)

    return app
