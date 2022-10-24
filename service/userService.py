from models.user import User

class UserService(object):
    
    def __init__(self):
        pass

    def register(self, username, password, args,admin=False):
        
        is_exist = False
        is_success = False

        if self.find_user(username):
          is_exist = True
          return is_exist,is_success


        if self.create_user(username,password,args,admin):
            is_success = True
        
        return is_exist,is_success
    

    def login(self, username, password):

        is_exist = True
        is_correct = True

        user = self.find_user(username)
        # print(user)
        # 后续需要做用户审核激活判断
        if user:
        # if user and user.active == 1:
            if not user.verify_password(password):
               is_correct = False
        else:
            is_exist = False
        
        return is_exist,is_correct, user
        # pass

    
    def find_user(self, username):

        # 可以先从cache 获取
        # todo 

        return User.query.filter(User.username == username).first()
        # pass 

    def find_user_by_id(self, id):
        return User.query.filter(User.id == id).first()

    def edit_user(self, username,args):
        
        user = self.find_user(username)

        if user == None:
            return False,False,False


        if args.get('password'):
            old_password = args.get('old_password')
            if not user.verify_password(old_password):
                return False,False,False
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

        return True,True,True
        

    def create_user(self, username, password, args,admin=False):
        is_success = False
        
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
        is_success = True
        
        return is_success

    def is_admin(self,username):

        user = self.find_user(username)

        if not user:
            return False

        if user.role_id != 1:
            return False
        
        return True