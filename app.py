from flask import Flask
from flask_restful import Api
from resource.route import initialize_routes
from database.db import initialize_db
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY']='Hacking99'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


initialize_db(app)
jwt = JWTManager(app)
initialize_routes(api)


if __name__ == '__main__':
    app.run(debug=True)
