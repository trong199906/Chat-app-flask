from flask import request, Response, jsonify
from flask_restful import Resource
import datetime
import sqlite3
from flask_jwt_extended import jwt_required, get_jwt_identity
from .json import dict_factory


class create_message(Resource):
    @jwt_required()
    def post(self):
        data = request.get_json(force=True)
        conn = sqlite3.connect('auth.db')
        cursor = conn.cursor()
        message = "INSERT INTO message values(NULL,?,?,?,?)"
        cursor.execute(message, (data['content'], data['creat_at'], data['user_1'], data['user_2']))
        conn.commit()
        conn.close()
        return jsonify({"message":"send message successful"})


class chat(Resource):
    @jwt_required()
    def get(self, id):
        conn = sqlite3.connect('auth.db')
        conn.row_factory = dict_factory
        cursor = conn.cursor()
        name = get_jwt_identity()[0][0]
        q1 = f"select id from user where name='{name}'"
        result_id = cursor.execute(q1).fetchone()
        user_1 = result_id['id']
        user_2 = id
        message_1 = f"select u1.name as name1, u2.name as name2, message.content, message.creat_at from message INNER JOIN user as u1 on  u1.id = message.user_1 INNER JOIN user as u2 on  u2.id = message.user_2 WHERE ((user_1 = {user_1} and user_2 = {user_2}) or (user_1={user_2} and user_2 = {user_1}))"
        user_info_1 = cursor.execute(message_1).fetchall()
        conn.commit()
        conn.close()
        return {"user_info_1": user_info_1}

