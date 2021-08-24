from flask import request, Response, jsonify
from flask_restful import Resource
from database.model import Friends, Users
from database.db import db
import datetime


class created_friend(Resource):
    def post(self):
        data = request.get_json(force=True)
        friends = Friends(**data)
        db.create_all()
        db.session.add(friends)
        db.session.commit()
        return jsonify({'message': 'created a friend'})


class get_all_list_friends(Resource):
    def get(self):
        friends = Friends.query.all()
        output = []
        for ls in friends:
            data = {}
            data['id'] = ls.id
            data['name'] = ls.name
            output.append(data)
        return jsonify({"list of fr": output})

