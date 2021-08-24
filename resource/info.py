from flask import request, Response, jsonify, json
from flask_restful import Resource
from sqlalchemy.orm import joinedload

from database.db import db
from database.model import Users, Friends


class get_info(Resource):
    def get(self):
        users = Users.query.all()
        friends = Friends.query.all()
        for ls in friends:
            data = {}
            data['id'] = ls.id
            data['name'] = ls.name
            users.append(data)
        print(users)