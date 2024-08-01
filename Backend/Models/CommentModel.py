from datetime import datetime
from . import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'), nullable=False)
    created_At = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_At = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)