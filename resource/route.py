from .auth import signup_user, login_user

def initialize_routes(api):
    api.add_resource(signup_user, '/api/auth/signup')
    api.add_resource(login_user, '/api/auth/login')