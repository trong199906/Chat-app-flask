import datetime

from .db import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))
    group_chat = db.relationship('Group_chat',lazy='dynamic')


class Group_chat(db.Model):
    chat_id = db.Column(db.Integer, primary_key=True)
    add_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    name_chat = db.Column(db.String(50))
    box_chat = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())

