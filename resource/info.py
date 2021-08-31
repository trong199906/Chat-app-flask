import sqlite3
from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from .json import dict_factory


class info(Resource):
    @jwt_required()
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
    @jwt_required()
    def get(self):
        conn = sqlite3.connect('auth.db')
        conn.row_factory = dict_factory
        cursor = conn.cursor()
        name = get_jwt_identity()
        info = "SELECT user.id , user.name,  info.user_2 from user INNER JOIN info on user.id = info.user_1 where name=?"
        user_info = cursor.execute(info, (name[0][0],)).fetchall()
        conn.commit()
        conn.close()
        return jsonify({"user_id": user_info})
