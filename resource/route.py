from .auth import signup_user, login_user
from .info import info, check_friend

def initialize_routes(api):
    api.add_resource(signup_user, '/api/auth/signup')
    api.add_resource(login_user, '/api/auth/login')

    api.add_resource(info, '/api/account/created-info')
    api.add_resource(check_friend, '/api/check-friend')