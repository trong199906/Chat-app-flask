from flask import request, jsonify, make_response
from flask_restful import Resource
from database.model import Users
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from database.db import db
from datetime import timedelta, datetime



class signup_user(Resource):
    def post(self):
        data = request.get_json(force=True)
        hashed_password = generate_password_hash(data['password'], method='sha256')
        new_user = Users(name=data['name'], password=hashed_password)

        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'registered successfully'})


class login_user(Resource):
    def post(self):
        auth = request.authorization

        if not auth or not auth.username or not auth.password:
            return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})

        user = Users.query.filter_by(name=auth.username).first()

        if check_password_hash(user.password, auth.password):
            expire_data = timedelta(days=7)
            token = create_access_token(
                identity=str(user.id),expires_delta=expire_data)
            return {'token': token}, 200
        return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})
