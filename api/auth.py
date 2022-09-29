
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token


from utils import response
from service import user_service

class Register(Resource):
    def post(self):

        args = reqparse.RequestParser() \
            .add_argument('username', type=str, location='form', required=True, help="用户名不能为空") \
            .add_argument("password", type=str, location='form', required=True, help="密码不能为空") \
            .add_argument("name", type=str, location='form') \
            .add_argument("phone", type=str, location='form') \
            .add_argument("email", type=str, location='form') \
            .parse_args()
        is_exist,is_success =  user_service.register(args['username'], args['password'],args)
        if is_exist == True:
            code = 201
            message = "user existed"
            return response(200,code=code, message=message)
        elif is_success == False:
            code = 203
            message = "register internal error"
            return response(504,code=code, message=message)
        
        code = 200
        message = "register successfully"
        return response(200,code=code, message=message)

        # return "register successfully",200

class Login(Resource):
    
    def post(self):
       
        args = reqparse.RequestParser() \
            .add_argument('username', type=str, location='form', required=True, help="用户名不能为空") \
            .add_argument("password", type=str, location='form', required=True, help="密码不能为空") \
            .parse_args()

        is_exist, is_correct, user = user_service.login(args['username'], args['password'])
        if not is_exist:
            code = 201
            message = "user not exist"
            return response(200,code=code, message=message)
        elif not is_correct:
            code = 202
            message = "wrong password"
            return response(200,code=code, message=message)
        else:
            code = 200
            message = "login successfully"
            data = {
                "token":create_access_token(identity=user.username),
                "user_id":user.id
            }
            return response(200,code=code, message=message, data=data)
