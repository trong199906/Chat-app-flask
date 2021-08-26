from flask import Flask
from flask_restful import Api
from resource.route import initialize_routes
from flask_jwt_extended import JWTManager


app = Flask(__name__)
jwt = JWTManager(app)
api = Api(app)
app.config['SECRET_KEY'] = 'super-secret'


initialize_routes(api)


if __name__ == '__main__':
    app.run(debug=True)
