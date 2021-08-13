from flask import request, jsonify, make_response
from flask_restful import Resource
import app
from database.model import Users
from werkzeug.security import generate_password_hash, check_password_hash
from database.db import db
import uuid
import jwt
import datetime



class signup_user(Resource):
    def post(self):
        data = request.get_json(force=True)
        hashed_password = generate_password_hash(data['password'], method='sha256')
        new_user = Users(public_id=str(uuid.uuid4()), name=data['name'], password=hashed_password)
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
            app_config = app.app.config
            token = jwt.encode(
                {'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},app_config['SECRET_KEY'])
            # return jsonify({'token': token.decode('utf-8')})
            return jsonify({'token': token})

        return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})
