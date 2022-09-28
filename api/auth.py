
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token


from utils import response
from service import user_service

class Register(Resource):
    def post(self):

        args = reqparse.RequestParser() \
            .add_argument('username', type=str, location='json', required=True, help="用户名不能为空") \
            .add_argument("password", type=str, location='json', required=True, help="密码不能为空") \
            .add_argument("name", type=str, location='json') \
            .add_argument("phone", type=str, location='json') \
            .add_argument("email", type=str, location='json') \
            .parse_args()

        is_exist,is_success =  user_service.register(args['username'], args['password'],args)
        if is_exist == True:
            code = 201
            message = "user existed"
            return response(code=code, message=message),200
        elif is_success == False:
            code = 203
            message = "register internal error"
            return response(code=code, message=message),504
        
        code = 200
        message = "register successfully"
        return response(code=code, message=message),200

        # return "register successfully",200

class Login(Resource):
    
    def post(self):
       
        args = reqparse.RequestParser() \
            .add_argument('username', type=str, location='json', required=True, help="用户名不能为空") \
            .add_argument("password", type=str, location='json', required=True, help="密码不能为空") \
            .parse_args()

        is_exist, is_correct, user = user_service.login(args['username'], args['password'])
        if not is_exist:
            code = 201
            message = "user not exist"
            return response(code=code, message=message),200
        elif not is_correct:
            code = 202
            message = "wrong password"
            return response(code=code, message=message),200
        else:
            code = 200
            message = "login successfully"
            data = {
                "token":create_access_token(identity=user.username),
                "user_id":user.id
            }
            return response(code=code, message=message, data=data),200
