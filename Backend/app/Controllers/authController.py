from flask import Blueprint, request, jsonify
from app.Models.UserModel import User
from app import db, bcrypt
from flask_jwt_extended import create_access_token, jwt_required

auth_controller = Blueprint('auth', __name__)

@auth_controller.route('/register', methods=['POST'])
def register():
    data = request.json

    # Validate email
    if not User.is_valid_email(data['email']):
        return jsonify({'message': 'Invalid email address'}), 400

    # Check if email or username already exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already registered'}), 400
    if not User.is_unique_username(data['username']):
        return jsonify({'message': 'Username already taken'}), 400

    # Validate password
    if not User.is_valid_password(data['password']):
        return jsonify({'message': 'Password must be at least 8 characters long and contain at least one number and one special character'}), 400

    # Hash the password
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    # Create and save the new user
    new_user = User(username=data['username'], email=data['email'], password=hashed_password)
    new_user.save()

    return jsonify({'message': 'User registered successfully'}), 201

@auth_controller.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    return jsonify({'message': 'Invalid credentials'}), 401


