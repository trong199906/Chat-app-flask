from flask import request, Response, jsonify
from flask_restful import Resource
from database.model import Users, Group_chat
from flask_jwt_extended import jwt_required
from database.db import db
import datetime

class create_group_chat(Resource):
    def get(self):
        group_chat = Group_chat.query.all().to_json()
        return Response(group_chat, mimetype="application/json", status=200)

    @jwt_required()
    def post(self):
        user_id = Users.id
        data = request.get_json()
        user = Users.query.get(id=user_id)
        group_chat = Group_chat(**data, add_by=user)
        db.session.add(group_chat)
        db.session.commit()
        return jsonify({"message": "successful to created a message"})

class chat(Resource):
    @jwt_required()
    def put(self,chat_id):
        user_id = Users.id
        group_chat = Group_chat.query.get(chat_id=chat_id, add_by=user_id)
        if not group_chat:
            return jsonify({"message": "doesnt exist group chat"})
        data = request.get_json()
        Group_chat.query.get(chat_id=chat_id).update(**data)
        return jsonify({"message": "update a message"})

    @jwt_required()
    def delete(self, chat_id):
        user_id = Users.id
        group_chat = Group_chat.query.get(chat_id=chat_id, add_by=user_id)
        if not group_chat:
            return jsonify({"message": "doesnt exist group chat"})
        db.session.delete(group_chat)
        db.session.commit()
        return jsonify({"message": "chat deleted"})

    @jwt_required()
    def get(self, chat_id):
        group_chat = Group_chat.query.get(chat_id=chat_id)
        return Response(group_chat, mimetype="application/json", status=200)





