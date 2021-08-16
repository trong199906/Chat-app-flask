from .auth import signup_user, login_user
from .chat import create_group_chat, chat

def initialize_routes(api):
    api.add_resource(signup_user, '/api/auth/signup')
    api.add_resource(login_user, '/api/auth/login')

    api.add_resource(create_group_chat, 'api/group-chat')
    api.add_resource(chat, 'api/chat/<int: chat_id>')