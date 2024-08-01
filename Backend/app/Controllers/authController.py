from flask import Blueprint, request, jsonify
from app.Models.UserModel import User
from app import db, bcrypt, jwt
from flask_jwt_extended import create_access_token, jwt_required, JWTManager, get_jwt

auth_controller = Blueprint('auth', __name__)
BLACKLIST = set()

@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in BLACKLIST

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
        return jsonify({
            'message': 'Login successful',
            'access_token': access_token
        }), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@auth_controller.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    try:
        jti = get_jwt()['jti']
        BLACKLIST.add(jti)
        return jsonify({"message": "Successfully logged out"}), 200
    except Exception as e:
        return jsonify({"message": "Logout failed", "error": str(e)}), 500


