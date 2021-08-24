from .auth import signup_user, login_user
from .friend import created_friend, get_all_list_friends
from .info import get_info

def initialize_routes(api):
    api.add_resource(signup_user, '/api/auth/signup')
    api.add_resource(login_user, '/api/auth/login')

    api.add_resource(get_all_list_friends, '/api/list-friend')
    api.add_resource(created_friend, '/api/created-friend')

    api.add_resource(get_info, '/api/account/info')
