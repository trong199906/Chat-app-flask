from flask import request, Response, jsonify
from flask_restful import Resource
import datetime
import sqlite3


class create_message(Resource):
    def post(self):
        data = request.get_json(force=True)
        conn = sqlite3.connect('auth.db')
        cursor = conn.cursor()
        message = "INSERT INTO message values(NULL,?,?,?,?)"
        cursor.execute(message, (data['content'],data['creat_at'],data['user_1'], data['user_2']))
        conn.commit()
        conn.close()
        return {"message":"send message successful"}


class chat(Resource):
    def get(self):
        conn = sqlite3.connect('auth.db')
        cursor = conn.cursor()
        message = "SELECT user.id , user.name, message.content, message.creat_at ,  message.user_2 from user INNER JOIN message on user.id = message.user_1"
        user_info = cursor.execute(message).fetchall()
        conn.commit()
        conn.close()
        return {"message": user_info}

