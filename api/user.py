from flask_restful import Resource, Api,reqparse
from flask_jwt_extended import get_jwt_identity,jwt_required

from models import user
from service import user_service
from utils import response
from utils.code import StatusCode


class Users(Resource):
    def get(self):
        return 'get users',200

class User(Resource):

    @jwt_required()
    def get(self):
        username = get_jwt_identity()

        user = user_service.find_user(username)

        if user == None:
            return response(400,StatusCode.USER_ERR.code,StatusCode.USER_ERR.message)
        else:
            print(user)
            data = {
                "username": user.username,
                "phone": user.phone,
                "name": user.name,
                "scores": user.scores,
                "active":user.active
            }
            return response(200,StatusCode.OK.code, StatusCode.OK.message,data)

            

    @jwt_required()
    def put(self):

        username = get_jwt_identity()

        args = reqparse.RequestParser() \
            .add_argument("old_password", type=str, location="json") \
            .add_argument("password", type=str, location="json") \
            .add_argument("phone", type=str, location="json") \
            .add_argument("name", type=str, location="json") \
            .add_argument("scores", type=int, location="json") \
            .add_argument("active",type=bool, location="json") \
            .parse_args()

        args = dict(args)

        flag1,flag2,flag3 = user_service.edit_user(username,args)

        if flag1 == False:
            return response(400,StatusCode.USER_ERR.code,StatusCode.USER_ERR.message)
        elif flag2 == False:
            return response(400,StatusCode.PWD_ERR.code,StatusCode.PWD_ERR.message)
        else:
            return response(200,StatusCode.OK.code,StatusCode.OK.message)
        
        # return "edit user user_id=%s" % user_id, 200

