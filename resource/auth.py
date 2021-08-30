from flask import request, jsonify, make_response
from flask_restful import Resource
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from datetime import timedelta, datetime
import sqlite3


class signup_user(Resource):
    def post(self):
        data = request.get_json(force=True)
        conn = sqlite3.connect('auth.db')
        cursor = conn.cursor()
        hashed_password = generate_password_hash(data['password'], method='sha256')
        q1 = "INSERT INTO user values (NULL,?,?,?)"
        cursor.execute(q1, (data['name'], data['email'], hashed_password))
        conn.commit()
        conn.close()
        return jsonify({'message': 'registered successfully'})


class login_user(Resource):
    def post(self):
        conn = sqlite3.connect('auth.db')
        cursor = conn.cursor()
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})
        name = auth.username
        q1 = "SELECT name, password from user where name=?"
        q2 = "SELECT password from user where name=?"
        expire_data = timedelta(days=7)
        cursor.execute(q1, (name,))
        users = cursor.fetchall()
        cursor.execute(q2, (name,))
        pwhash = cursor.fetchone()
        if check_password_hash(pwhash[0], password=auth.password):
            token = create_access_token(identity=users, expires_delta=expire_data, fresh=True)
            return {"token":token},200
        conn.close()
        return make_response('could not verify',  401, {'WWW.Authentication': 'Basic realm: "login required"'})

