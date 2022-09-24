from flask_restful import Resource, Api


class Users(Resource):
    def get(self):
        return 'get users',200

class User(Resource):


    def get(self, user_id):
        return "get user user_id=%s" % user_id, 200

    def put(self,user_id):
        return "edit user user_id=%s" % user_id, 200

