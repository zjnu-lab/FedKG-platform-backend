from models.user import User

class UserService:
    
    def __init__(self):
        pass

    def register(self, username, password, **kwargs):
        
        is_exist = False
        is_success = False

        if self.get_user(username):
          is_exist = True

        if self.create_user(username,password,kwargs):
            is_success = True
        
        return is_exist,is_success

    def login(self, username, password):

        is_exist = True
        is_correct = True

        user = self.get_user(username)
        if user and user.active == 1:
            if not user.check_password_hash(password):
               is_correct = False
        else:
            is_exist = False
        
        return is_exist,is_correct, user
        # pass

    
    def get_user(self, username):

        # 可以先从cache 获取
        # todo 

        return User.query.filter(User.username == username).first()
        # pass 

    def edit_user(self, username,**kwargs):
        pass

    def create_user(self, username, password, **kwargs):
        new_user = User(username,password)
        if kwargs.get('phone'):
            new_user.phone = kwargs.get('phone')
        if kwargs.get('email'):
            new_user.email = kwargs.get('email')
        if kwargs.get('name'):
            new_user.name = kwargs.get('name')
        
        
        new_user.save_to_db()