from flask_restful import Resource, Api


from service.userService import UserService

user_service = UserService()

class Register(Resource):
    def post(self):

        args = reqparse.RequestParser() \
            .add_argument('username', type=str, location='json', required=True, help="用户名不能为空") \
            .add_argument("password", type=str, location='json', required=True, help="密码不能为空") \
            .parse_args()

        flag_user_exit,flag_register_sucess =  user_service.register(args['username'], args['password'])
        if flag_user_exit == True:
            pass 
        elif flag_register_sucess == True:
            pass 
        elif flag_register_sucess == False:
            pass

        return "register successfully",200

class Login(Resource):
    # def post(self):
    #     return "login successfully",200
    def post(self):
        code = None
        message = None
        token = None
        userid = None

        args = reqparse.RequestParser() \
            .add_argument('username', type=str, location='json', required=True, help="用户名不能为空") \
            .add_argument("password", type=str, location='json', required=True, help="密码不能为空") \
            .parse_args()

        flag_user_exist, flag_password_correct, user = user_service.login(args['username'], args['password'])
        if not flag_user_exist:
            code = 201
            message = "user not exist"
        elif not flag_password_correct:
            code = 202
            message = "wrong password"
        else:
            code = 200
            message = "success"
            token = create_access_token(identity=user.username)
            userid = user.id

        return jsonify({
            "code": code,
            "message": message,
            "token": token,
            "userid": userid
        })

