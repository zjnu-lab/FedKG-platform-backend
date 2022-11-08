from xxlimited import Str
from flask_restful import Resource, Api,reqparse
from flask_jwt_extended import get_jwt_identity,jwt_required

from models import user
from service import node_service,graph_service
from utils import response
from utils.code import StatusCode


class KGraph(Resource):

    @jwt_required()
    def get(self):

        code,nodes,links = graph_service.get_init_graph()

        if code == StatusCode.OK:
            data ={
                "nodes": nodes,
                "links": links
            }
            return response(200,code.code,code.message,data)
        else:
            return response(400,code.code,code.message)
        

class Node(Resource):

    @jwt_required()
    def get(self):

        args = reqparse.RequestParser() \
            .add_argument('node_name', type=str, location='args') \
            .parse_args()

        node_name = args.get('node_name')

        code,node = node_service.get_node_by_name(node_name)

        if code == StatusCode.OK:
            data = {
                # "node_id":  node['id'],
                # "node_name": node['name'],
                "node_attr": dict(node),
            }
            return response(200,code.code,code.message,data)
        else:
            return response(400,code.code,code.message)

    @jwt_required()
    def post(self):

        pass

class Nodes(Resource):

    @jwt_required()
    def get(self):
       pass

    @jwt_required()
    def post(self):

        pass

class Relationship(Resource):

    @jwt_required()
    def get(self):
        pass

class Search(Resource):

    @jwt_required()
    def get(self):
        args = reqparse.RequestParser() \
            .add_argument('node_name', type=str, location='args') \
            .parse_args()

        node_name = args.get('node_name')

        # code,node = node_service.get_node_by_name(node_name)
        code,nodes = graph_service.fuzzy_search(node_name)

        if code == StatusCode.OK:
            data = {}
            node_list = []
            for node in nodes:
                node_list.append(node)
            data = {
                # "node_id":  node['id'],
                # "node_name": node['name'],
                "node_list": node_list,
            }
            return response(200,code.code,code.message,data)
        else:
            return response(400,code.code,code.message)


class OnehopNeighbor(Resource):

    @jwt_required()
    def get(self):
        args = reqparse.RequestParser() \
            .add_argument('node_id', type=str, location='args') \
            .add_argument('limits', type=str, location='args') \
            .parse_args()

        node_id = args.get('node_id')
        
        if args.get('limits'):
            limits = args.get('limits')
            code,nodes,links = graph_service.get_one_hop_neighbor(node_id,limits)
        else:
            code,nodes,links = graph_service.get_one_hop_neighbor(node_id)

        if code == StatusCode.OK:
            data = {
                "nodes": nodes,
                "links": links
            }

            return response(200,code.code,code.message,data)
        else:
            return response(400,code.code,code.message)

class TwohopNeighbor(Resource):

    @jwt_required()
    def get(self):
        args = reqparse.RequestParser() \
            .add_argument('node_id', type=str, location='args') \
            .add_argument('limits', type=str, location='args') \
            .parse_args()

        node_id = args.get('node_id')
        
        if args.get('limits'):
            limits = args.get('limits')
            code,nodes,links = graph_service.get_two_hop_neighbor(node_id,limits)
        else:
            code,nodes,links = graph_service.get_two_hop_neighbor(node_id)


        if code == StatusCode.OK:
            data = {
                "nodes": nodes,
                "links": links
            }

            return response(200,code.code,code.message,data)
        else:
            return response(400,code.code,code.message)



