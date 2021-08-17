from flask import request, Response, jsonify
from flask_restful import Resource
from database.model import Users, Group_chat
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.db import db
import datetime

class create_group_chat(Resource):
    def get(self):
        group_chat = Group_chat.query.all()
        output = []
        for group_data in group_chat:
            data = {}
            data['chat_id']= group_data.chat_id
            data['add_by']= group_data.add_by
            data['name_chat']= group_data.name_chat
            data['box_chat']= group_data.box_chat
            data['created_at']= group_data.created_at
            output.append(data)
        return jsonify({"list of message": output})

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        data = request.get_json(force=True)
        group_chat = Group_chat(**data, add_by=user_id)
        db.create_all()
        db.session.add(group_chat)
        db.session.commit()
        return jsonify({"message": "successful to created a message"})

class chat(Resource):
    @jwt_required()
    def put(self,chat_id):
        data = request.get_json()
        group_chat = Group_chat.query.get(chat_id)
        if not group_chat:
            return jsonify({"message": "doesnt exist group chat"})
        if data.get('name_chat'):
            group_chat.name_chat = data['name_chat']
        if data.get('box_chat'):
            group_chat.box_chat = data['box_chat']
        db.session.add(group_chat)
        db.session.commit()
        return jsonify({"message": "update a message"})

    @jwt_required()
    def delete(self, chat_id):
        group_chat = Group_chat.query.get(chat_id)
        if not group_chat:
            return jsonify({"message": "doesnt exist group chat"})
        db.session.delete(group_chat)
        db.session.commit()
        return jsonify({"message": "chat deleted"})

    @jwt_required()
    def get(self, chat_id):
        group_chat = Group_chat.query.filter_by(chat_id=chat_id)
        output = []
        for group_data in group_chat:
            data = {}
            data['chat_id'] = group_data.chat_id
            data['add_by'] = group_data.add_by
            data['name_chat'] = group_data.name_chat
            data['box_chat'] = group_data.box_chat
            data['created_at'] = group_data.created_at
            output.append(data)
        return jsonify({"chat id": output})




