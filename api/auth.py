
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token


from utils import response
from utils.code import StatusCode
from service import user_service

class Register(Resource):
    def post(self):

        args = reqparse.RequestParser() \
            .add_argument('username', type=str, location='form', required=True, nullable = False, help="用户名不能为空") \
            .add_argument("password", type=str, location='form', required=True, nullable = False, help="密码不能为空") \
            .add_argument("name", type=str, location='form') \
            .add_argument("phone", type=str, location='form') \
            .add_argument("email", type=str, location='form') \
            .parse_args()
        
        if args['username'] == "":
            return response(400,code=StatusCode.USER_NULL.code,message=StatusCode.USER_NULL.message)

        if args['password'] == "":
            return response(400,code=StatusCode.PWD_NULL.code,message=StatusCode.PWD_NULL.message)
        
        is_exist,is_success =  user_service.register(args['username'], args['password'],args)

        if is_exist == True:
            return response(200,code=StatusCode.USER_EXISTED.code, message=StatusCode.USER_EXISTED.message)
        elif is_success == False:
            return response(500,code=StatusCode.ERROR.code, message=StatusCode.ERROR.message)
        
        return response(200,code=StatusCode.RESGISTER_SUCCESS.code, message=StatusCode.RESGISTER_SUCCESS.message)

        # return "register successfully",200

class Login(Resource):
    
    def post(self):
       
        args = reqparse.RequestParser() \
            .add_argument('username', type=str, location="form", required=True, help="用户名不能为空") \
            .add_argument("password", type=str, location="form", required=True, help="密码不能为空") \
            .parse_args()

        is_exist, is_correct, user = user_service.login(args['username'], args['password'])
        if not is_exist:
            return response(400,code=StatusCode.USER_ERR.code, message=StatusCode.USER_ERR.message)
        elif not is_correct:
            return response(400,code=StatusCode.PWD_ERR.code, message=StatusCode.PWD_ERR.message)
        else:
            data = {
                "token":create_access_token(identity=user.username),
                "user_id":user.id
            }
            return response(200,code=StatusCode.Login_SUCCESS.code, message=StatusCode.Login_SUCCESS.message, data=data)
