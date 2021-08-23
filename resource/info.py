from flask import request, Response, jsonify
from flask_restful import Resource
from sqlalchemy.orm import joinedload

from database.db import db
from database.model import Users, Friends


class get_info(Resource):
    def get(self):
        a = 1
        pass