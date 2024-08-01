from flask import Blueprint

auth_views = Blueprint('auth_views', __name__)

@auth_views.route('/login')
def login():
    return "login"

@auth_views.route('/register')
def register():
    return "register"