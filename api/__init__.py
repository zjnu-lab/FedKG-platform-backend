import sys
from flask_restful import Resource, Api

from api.hello import Hello
from api.auth import Register,Login,AdminRegister,Refresh
from api.user import User,Users

from api.new_entity import NewEntity,UserNewEntities,Review
from api.grpah import KGraph, Node,NodeId ,Search, OnehopNeighbor,TwohopNeighbor
from api.file import File

from api.task import Task,Tasks,UserTasks

from api.model import Model,Models,UserModels,ModelName

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
    api.add_resource(Refresh, '/refresh')

    #new_entity
    api.add_resource(NewEntity, '/user/newent')

    #user_new_entities
    api.add_resource(UserNewEntities, '/user/newents')

    #review
    api.add_resource(Review,'/review')

    #kgGraph
    api.add_resource(Node,'/node')
    api.add_resource(NodeId,'/nodeid')
    api.add_resource(KGraph,'/initgraph')
    api.add_resource(Search,'/search')
    api.add_resource(OnehopNeighbor, '/node/onehop')
    api.add_resource(TwohopNeighbor, '/node/twohop')

    #file
    api.add_resource(File,'/file')

    #task
    api.add_resource(Task,'/task')
    api.add_resource(Tasks,'/tasks')
    api.add_resource(UserTasks,'/usertasks')


    #models
    api.add_resource(Model,'/model')
    api.add_resource(ModelName,'/modelname')
    api.add_resource(UserModels,'/usermodels')
    api.add_resource(Models,'/modellist')

