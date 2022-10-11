import sys
from flask_restful import Resource, Api

from api.hello import Hello
from api.auth import Register,Login
from api.user import User,Users

def register_api(app):

    api = Api(app)

    #hello_world
    api.add_resource(Hello, '/')
    

    #user
    api.add_resource(Users, '/users')
    api.add_resource(User, '/user/<user_id>')


    #auth
    api.add_resource(Login, '/login')
    api.add_resource(Register, '/register')