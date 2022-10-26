from models.user import User
from utils.code import StatusCode

class UserService(object):
    
    def __init__(self):
        pass

    def register(self, username, password, args,admin=False):
        '''用户注册服务
        
        :username: 用户名(邮箱)
        :password: 密码
        :args: 注册的用户信息
        :admin: 是否注册管理员
        '''
        
        _, user = self.find_user(username)
        if user is not None:
            return StatusCode.USER_EXISTED

        return self.create_user(username,password,args,admin)
            
        
        
    

    def login(self, username, password):
        '''用户登录服务
        
        :username: 用户名(邮箱)
        :password: 密码
        :return: StatusCode,user
        '''

        code,user = self.find_user(username)
        # print(user)
        # 后续需要做用户审核激活判断
        if user:
        # if user and user.active == 1:
            if not user.verify_password(password):
                return StatusCode.PWD_ERR,None
            else:
                return StatusCode.Login_SUCCESS,user
        else:
            return code,None


    
    def find_user(self, username):
        '''查找用户
        
        :username: 用户名(邮箱)
        :return: StatusCode,user
        '''

        # 可以先从cache 获取
        # todo 
        user = User.query.filter(User.username == username).first()
        if user == None:
            return StatusCode.USER_ERR,None
        else:
            return StatusCode.OK,user
        # return User.query.filter(User.username == username).first()
        # pass 

    def find_user_by_id(self, id):
        '''通过用户id 查找用户'''
        return User.query.filter(User.id == id).first()

    def edit_user(self, username,args):
        '''修改用户信息
        
        :username: 用户名(邮箱)
        :password: 密码
        :args: 修改的属性
        :return: StatusCode
        '''
        
        code,user = self.find_user(username)

        if user == None:
            return code


        if args.get('password'):
            old_password = args.get('old_password')
            if not user.verify_password(old_password):
                # return False,False,False
                return StatusCode.PWD_ERR
            user.password = args.get('password')
        if args.get('phone'):
            user.phone = args.get('phone')
        if args.get('email'):
            user.email = args.get('email')
        if args.get('name'):
            user.name = args.get('name')
        if args.get('scores'):
            user.scores = args.get('scores')
        if args.get('active'):
            user.active = args.get('active')


        user.save_to_db()

        return StatusCode.OK
        

    def create_user(self, username, password, args,admin=False):
        '''创建用户
        
        :username: 用户名(邮箱)
        :password: 密码
        :args: 注册用户属性
        :admin: 是否注册管理员
        :return: StatusCode
        '''
        
        new_user = User(username,password)

        if args.get('phone'):
            new_user.phone = args.get('phone')
        if args.get('email'):
            new_user.email = args.get('email')
        if args.get('name'):
            new_user.name = args.get('name')
        if args.get('organization'):
            new_user.organization = args.get('organization')
        
        if admin == True:
            new_user.role_id = 1
            new_user.active = True
        
        new_user.save_to_db()
        
        return StatusCode.RESGISTER_SUCCESS

    def is_admin(self,username):
        '''判断是否是管理员用户
        
        :username: 用户名(邮箱)
        :return: StatusCode
        '''

        code,user = self.find_user(username)

        if not user:
            return code

        if user.role_id != 1:
            return StatusCode.ADMIN_ERR
        
        return StatusCode.OK