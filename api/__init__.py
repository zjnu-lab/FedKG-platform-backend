import sys
from flask_restful import Resource, Api

from api.hello import Hello
from api.auth import Register,Login,AdminRegister
from api.user import User,Users

from api.new_entity import NewEntity,UserNewEntities,Review
from api.grpah import KGraph, Node

def register_api(app):

    api = Api(app)

    #hello_world
    api.add_resource(Hello, '/')
    

    #user
    api.add_resource(Users, '/users')
    api.add_resource(User, '/userinfo')


    #auth
    api.add_resource(Login, '/login')
    api.add_resource(Register, '/register')
    api.add_resource(AdminRegister, '/admin/register')

    #new_entity
    api.add_resource(NewEntity, '/user/newent')

    #user_new_entities
    api.add_resource(UserNewEntities, '/user/newents')

    #review
    api.add_resource(Review,'/review')

    #kgGraph
    api.add_resource(Node,'/node')
    api.add_resource(KGraph,'/initgraph')
