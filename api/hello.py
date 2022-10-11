from tkinter.tix import Tree
from flask_restful import Resource, Api, reqparse
from flask import jsonify
import pickle


class Hello(Resource):
    def get(self):
        args = reqparse.RequestParser() \
            .add_argument('nwid', type=int, location='args',required = True) \
            .parse_args()

        return 'hello_world'+str(args["nwid"]),200

    def post(self):

        args = reqparse.RequestParser() \
            .add_argument('info', type = dict, required = True) \
            .parse_args()

        print(args)
        print(type(args))
        print(args.keys())
        print(type(dict(args)))
        

        p = pickle.dumps(dict(args))

        print(p)

        np = pickle.loads(p)

        print(np)

        print(np.keys())

        print(type(np))
        
        
        return jsonify(dict(args))



