from models.user import User

class UserService:
    
    def __init__(self):
        pass

    def register(self, username, password, **kwargs):
        
        flag_user_exist = False
        flag_register_success = False

        if self.get_user(username):
          flag_user_exist = True

        if self.create_user(username,password):
            flag_register_success = True
        
        return flag_user_exist,flag_register_success

    def login(self, username, password):

        flag_user_exist = True
        flag_password_correct = True

        user = self.get_user(username)
        if user and user.active == 1:
            if not user.check_password_hash(password):
                flag_password_correct = False
        else:
            flag_user_exist = False
        
        return flag_user_exist, flag_password_correct, user
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
        new_user.save_to_db()