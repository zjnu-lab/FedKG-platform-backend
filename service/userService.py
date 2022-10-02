from models.user import User

class UserService(object):
    
    def __init__(self):
        pass

    def register(self, username, password, args):
        
        is_exist = False
        is_success = False

        if self.find_user(username):
          is_exist = True
          return is_exist,is_success


        if self.create_user(username,password,args):
            is_success = True
        
        return is_exist,is_success

    def login(self, username, password):

        is_exist = True
        is_correct = True

        user = self.find_user(username)
        if user and user.active == 1:
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

    def edit_user(self, username,**kwargs):
        pass

    def create_user(self, username, password, args):
        is_success = False
        
        new_user = User(username,password)
        if args.get('phone'):
            new_user.phone = args.get('phone')
        if args.get('email'):
            new_user.email = args.get('email')
        if args.get('name'):
            new_user.name = args.get('name')
        
        
        new_user.save_to_db()
        is_success = True
        
        return is_success