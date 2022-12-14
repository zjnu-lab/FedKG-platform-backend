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

        code,user = user_service.find_user(username)

        if user == None:
            return response(400,code.code,code.message)
        else:
            # print(user)
            data = {
                "username": user.username,
                "phone": user.phone,
                "organization": user.organization,
                "name": user.name,
                "scores": user.scores,
                "active":user.active,
                # score_records 需要进行处理，这里先直接用
                "scores_records": user.score_records
            }
            return response(200,code.code, code.message,data)

            

    @jwt_required()
    def post(self):

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

        code = user_service.edit_user(username,args)

        if code == StatusCode.OK:
            return response(200,code.code,code.message)
        else:
            return response(400,code.code,code.message)


