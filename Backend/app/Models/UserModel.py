from datetime import datetime
from flask_login import UserMixin
from app import db,bcrypt
from werkzeug.security import generate_password_hash, check_password_hash
import re
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    created_At = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_At = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy=True, cascade="all, delete-orphan")
    comments = db.relationship('Comment', backref='author', lazy=True, cascade="all, delete-orphan")

    @staticmethod
    def is_valid_email(email):
        # Simple email regex validation
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    @staticmethod
    def is_valid_password(password):
        # Password must be at least 8 characters long and contain at least one number and one special character
        if len(password) < 8:
            return False
        if not any(c.isdigit() for c in password):
            return False
        if not any(c in '!@#$%^&*()' for c in password):
            return False
        return True

    @staticmethod
    def is_unique_username(username):
        return User.query.filter_by(username=username).first() is None

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
