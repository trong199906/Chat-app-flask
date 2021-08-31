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
    def get(self):
        conn = sqlite3.connect('auth.db')
        conn.row_factory = dict_factory
        cursor = conn.cursor()
        name = get_jwt_identity()
        message_1 = "select user.id , user.name , message.content, message.creat_at, message.user_2 from user INNER JOIN message on  user.id = message.user_1 where name=? and user_2=3 or name='anh' and user_2=1"
        user_info_1 = cursor.execute(message_1, (name[0][0],)).fetchall()
        conn.commit()
        conn.close()
        return {"user_info_1": user_info_1}

