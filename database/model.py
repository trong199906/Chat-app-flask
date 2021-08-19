import datetime

from .db import db

info = db.Table('info',
        db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
        db.Column('friend_id', db.Integer, db.ForeignKey('friends.id'), primary_key=True)
)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))
    friends = db.relationship('Friends', secondary='info', lazy="dynamic")

class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message_id = db.relationship('Messages', lazy="dynamic")
    name = db.Column(db.String(50))


class Messages(db.Model):
    friend_id = db.Column(db.ForeignKey('friends.id'))
    messages_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())