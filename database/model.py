import datetime
from .db import db

# info = db.table('user_info',
#         db.Column('users_id', db.Integer, db.ForeignKey('users.id')),
#         db.Column('friends_id', db.Integer, db.ForeignKey('friends.id'))
# )


class Users(db.Model):
    __name__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))
    friend_id = db.Column(db.Integer, db.ForeignKey("friends.id"))
    friend = db.relationship("Friends")
    # def __init__(self, name, password):
    #     self.name = name
    #     self.password = password


    def __repr__(self):
        return "{}:{}".format(self.id, self.name)


class Friends(db.Model):
    __name__='friends'
    id = db.Column(db.Integer, primary_key=True)
    # message_id = db.relationship('Messages', lazy="dynamic")
    # name = db.Column(db.String(50))
    list_friends = db.Column(db.String(255), default=None)


class Messages(db.Model):
    messages_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    friend_id = db.Column(db.ForeignKey('friends.id'))
    friend = db.relationship("Friends")