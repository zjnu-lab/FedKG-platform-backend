from flask_restful import Resource, Api


class Register(Resource):
    def post(self):
        return "register successfully",200

class Login(Resource):
    def post(self):
        return "login successfully",200
