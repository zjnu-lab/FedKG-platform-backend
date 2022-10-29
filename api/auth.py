
from api import user
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity



from utils import response,validate_email
from utils.code import StatusCode
from service import user_service

class Register(Resource):
    def post(self):

        args = reqparse.RequestParser() \
            .add_argument('username', type=str, location='json', required=True, nullable = False, help="用户名(默认为email)不能为空") \
            .add_argument("password", type=str, location='json', required=True, nullable = False, help="密码不能为空") \
            .add_argument("name", type=str, location='json') \
            .add_argument("phone", type=str, location='json') \
            .add_argument("email", type=str, location='json') \
            .add_argument("organization", type=str, location='json') \
            .parse_args()
        
        if args['username'] == "":
            return response(400,code=StatusCode.USER_NULL.code,message=StatusCode.USER_NULL.message)
        
        # 用户名必须为邮箱格式
        if validate_email(args['username']) == False:
            return response(400,code=StatusCode.USER_NULL.code,message=StatusCode.USER_NULL.message)

        if args['password'] == "":
            return response(400,code=StatusCode.PWD_NULL.code,message=StatusCode.PWD_NULL.message)
        
        code =  user_service.register(args['username'], args['password'],args)

        if code == StatusCode.RESGISTER_SUCCESS:
            return response(200,code.code,code.message)
        else:
            return response(400,code.code,code.message)

class Login(Resource):
    
    def post(self):
       
        args = reqparse.RequestParser() \
            .add_argument('username', type=str, location="json", required=True, help="用户名不能为空") \
            .add_argument("password", type=str, location="json", required=True, help="密码不能为空") \
            .parse_args()

        # print (args)

        if args['username'] == "":
            return response(400,code=StatusCode.USER_NULL.code,message=StatusCode.USER_NULL.message)

        if args['password'] == "":
            return response(400,code=StatusCode.PWD_NULL.code,message=StatusCode.PWD_NULL.message)

        code,user = user_service.login(args['username'], args['password'])

        if code == StatusCode.Login_SUCCESS:
            data = {
                "token":create_access_token(identity=user.username,fresh=False),
                "refresh_token":create_refresh_token(identity=user.username),
                "user_id":user.id,
                "user_role":user.role_id
            }
            return response(200,code.code,code.message,data)
        else:
            return response(400,code.code,code.message)
        
        
class AdminRegister(Resource):
    def post(self):

        args = reqparse.RequestParser() \
            .add_argument('username', type=str, location='json', required=True, nullable = False, help="用户名(默认为email)不能为空") \
            .add_argument("password", type=str, location='json', required=True, nullable = False, help="密码不能为空") \
            .add_argument("name", type=str, location='json') \
            .add_argument("phone", type=str, location='json') \
            .add_argument("email", type=str, location='json') \
            .parse_args()
        
        if args['username'] == "":
            return response(400,code=StatusCode.USER_NULL.code,message=StatusCode.USER_NULL.message)
        
        # 用户名必须为邮箱格式
        if validate_email(args['username']) == False:
            return response(400,code=StatusCode.USER_NULL.code,message=StatusCode.USER_NULL.message)

        if args['password'] == "":
            return response(400,code=StatusCode.PWD_NULL.code,message=StatusCode.PWD_NULL.message)
        
        code =  user_service.register(args['username'], args['password'],args,admin=True)

        if code == StatusCode.RESGISTER_SUCCESS:
            return response(200,code.code,code.message)
        else:
            return response(400,code.code,code.message)


class Refresh(Resource):
    
    @jwt_required(refresh=True)
    def post(self):
        username = get_jwt_identity()


        data = {
            "token":create_access_token(identity=username),
        }
        return response(200,StatusCode.OK.code,StatusCode.OK.message,data)

        