from flask_restful import Resource, Api


class Hello(Resource):
    def get(self):
        return 'hello_world',200
