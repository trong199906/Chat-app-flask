import sqlite3
from flask import request, jsonify, make_response
from flask_restful import Resource

class info(Resource):
    def post(self):
        data = request.get_json()
        conn = sqlite3.connect('auth.db')
        cursor = conn.cursor()
        info = "INSERT INTO info values(?,?)"
        cursor.execute(info, (data['user_1'], data['user_2']))
        conn.commit()
        conn.close()
        return jsonify({'info': 'info successfully'})


class check_friend(Resource):
    def get(self):
        conn = sqlite3.connect('auth.db')
        cursor = conn.cursor()
        info = "select user.id ,name, user_1, user_2 from user, info WHERE user.id = info.user_1 or user.id = info.user_2"
        user_info = cursor.execute(info).fetchone()
        conn.commit()
        conn.close()
        return jsonify({"info": user_info})