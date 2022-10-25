from models.user import User
from utils.code import StatusCode

class UserService(object):
    
    def __init__(self):
        pass

    def register(self, username, password, args,admin=False):
        
        _, user = self.find_user(username)
        if user is not None:
            return StatusCode.USER_EXISTED

        return self.create_user(username,password,args,admin)
            
        
        
    

    def login(self, username, password):

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
        return User.query.filter(User.id == id).first()

    def edit_user(self, username,args):
        
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
        
        new_user = User(username,password)

        if args.get('phone'):
            new_user.phone = args.get('phone')
        if args.get('email'):
            new_user.email = args.get('email')
        if args.get('name'):
            new_user.name = args.get('name')
        
        if admin == True:
            new_user.role_id = 1
            new_user.active = True
        
        new_user.save_to_db()
        
        return StatusCode.RESGISTER_SUCCESS

    def is_admin(self,username):

        code,user = self.find_user(username)

        if not user:
            return code

        if user.role_id != 1:
            return StatusCode.ADMIN_ERR
        
        return StatusCode.OK