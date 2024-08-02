from flask import Blueprint, request, jsonify
from app.Models.UserModel import User
from app import db, bcrypt, jwt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt

auth_controller = Blueprint('auth', __name__)
BLACKLIST = set()

@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in BLACKLIST

@auth_controller.route('/register', methods=['POST'])
def register():
    try:
        data = request.json

        # Validate email
        if not User.is_valid_email(data['email']):
            return jsonify({
                'message': 'Invalid email address',
                'status': False,
                'type': 'custom_error',
                'error_status': {'error_code': '40001'}
            }), 400

        # Check if email or username already exists
        if User.query.filter_by(email=data['email']).first():
            return jsonify({
                'message': 'Email already registered',
                'status': False,
                'type': 'custom_error',
                'error_status': {'error_code': '40001'}
            }), 400
        if not User.is_unique_username(data['username']):
            return jsonify({
                'message': 'Username already taken',
                'status': False,
                'type': 'custom_error',
                'error_status': {'error_code': '40001'}
            }), 400

        # Validate password
        if not User.is_valid_password(data['password']):
            return jsonify({
                'message': 'Password must be at least 8 characters long and contain at least one number and one special character',
                'status': False,
                'type': 'custom_error',
                'error_status': {'error_code': '40001'}
            }), 400

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

        # Create and save the new user
        new_user = User(username=data['username'], email=data['email'], password=hashed_password)
        new_user.save()

        return jsonify({
            'message': 'User registered successfully',
            'status': True,
            'type': 'success_message',
            'error_status': {'error_code': '00000'},
            'data': {
                'user_id': new_user.id,
                'username': new_user.username,
                'email': new_user.email,
            }
        }), 201
    except Exception as e:
        return jsonify({
            'message': 'Registration failed',
            'status': False,
            'type': 'custom_error',
            'error_status': {'error_code': '50000'},
            'error': str(e)
        }), 500

@auth_controller.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        user = User.query.filter_by(username=data['username']).first()

        if user and bcrypt.check_password_hash(user.password, data['password']):
            access_token = create_access_token(identity=user.id)
            return jsonify({
                'message': 'User logged in successfully',
                'status': True,
                'type': 'success_message',
                'error_status': {'error_code': '00000'},
                'data': {
                    'user_id': user.id,
                    'username': user.username,
                    'access_token': access_token
                }
            }), 200
        return jsonify({
            'message': 'Invalid input data',
            'status': False,
            'type': 'custom_error',
            'error_status': {'error_code': '40001'}
        }), 400
    except Exception as e:
        return jsonify({
            'message': 'Login failed',
            'status': False,
            'type': 'custom_error',
            'error_status': {'error_code': '50000'},
            'error': str(e)
        }), 500

@auth_controller.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    try:
        jti = get_jwt()['jti']
        BLACKLIST.add(jti)
        return jsonify({
            'message': 'Logout successful',
            'status': True,
            'type': 'success_message',
            'error_status': {'error_code': '00000'}
        }), 200
    except Exception as e:
        return jsonify({
            'message': 'Logout failed',
            'status': False,
            'type': 'custom_error',
            'error_status': {'error_code': '50000'},
            'error': str(e)
        }), 500
