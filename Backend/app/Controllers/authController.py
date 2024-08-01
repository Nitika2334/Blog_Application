from flask import Blueprint, request, jsonify
from app.Models.UserModel import User
from app import db
from flask_jwt_extended import create_access_token, jwt_required

auth_controller = Blueprint('auth', __name__)

@auth_controller.route('/register', methods=['POST'])
def register():
    try:
        data = request.json

        # Validate email
        if not User.is_valid_email(data['email']):
            return jsonify({'message': 'Invalid email address'}), 400

        # Check if email or username already exists
        if User.query.filter_by(email=data['email']).first():
            return jsonify({'message': 'Email already registered'}), 400
        if User.query.filter_by(username=data['username']).first():
            return jsonify({'message': 'Username already taken'}), 400

        # Validate password
        if not User.is_valid_password(data['password']):
            return jsonify({'message': 'Password must be at least 8 characters long and contain at least one number and one special character'}), 400

        # Create and save the new user
        new_user = User(username=data['username'], email=data['email'])
        new_user.set_password(data['password'])
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'}), 201

    except KeyError as e:
        return jsonify({'message': f'Missing required field: {str(e)}'}), 400
    except Exception as e:
        db.session.rollback()  # Rollback any changes if something goes wrong
        return jsonify({'message': 'An error occurred during registration'}), 500

@auth_controller.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        user = User.query.filter_by(email=data['email']).first()
        if user and user.check_password(data['password']):
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token), 200
        return jsonify({'message': 'Invalid credentials'}), 401

    except KeyError as e:
        return jsonify({'message': f'Missing required field: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'message': 'An error occurred during login'}), 500

@auth_controller.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    logout
    try:
        return jsonify({'message': 'Logout successful'}), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred during logout'}), 500
