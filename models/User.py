from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
import sys
print(sys.path)
from app import db
# from app import db, login_manager
# from flask_login import UserMixin
# from itsdangerous import TimedJSONWebSignatureSerializer
from datetime import datetime

# Flask中一个Model子类就是数据库中的一个表。默认表名'User'.lower() ===> user

class User(db.Model):

    __tablename__ = 'users'  # 自定义数据表的表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    active = db.Column(db.Boolean, default=True, nullable=False)
    # db.Boolean是布尔类型， 值只能是True或者False。
    # confirmed = db.Column(db.Boolean, default=False)  # 账户是否已经确认
    # 新添加的用户资料
    
    # 用户的真实姓名
    # location = db.Column(db.String(64))  # 所在地
    # about_me = db.Column(db.Text())  # 自我介绍
    # 注册日期
    # default 参数可以接受函数作为默认值,
    # 所以每次生成默认值时,db.Column() 都会调用指定的函数。
    # create_time = db.Column(db.DateTime, default=datetime.utcnow)
    # # 最后访问日期
    # last_seen = db.Column(db.DateTime(), default=datetime.utcnow)

    

    # 外键关联
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    # # 反向引用: 1). User添加属性todos   2). Todo添加属性user
    # todos = db.relationship('Todo', backref='user')
    # # 反向引用: 1). User添加属性categories   2). Category添加属性user
    # categories = db.relationship('Category', backref='user')


    def __init__(self, username=None, password=None, active=True):
        self.username = username
        self.password = password
        self.active = active

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        # generate_password_hash(password, method= pbkdf2:sha1 , salt_length=8):密码加密的散列值。
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        # check_password_hash(hash, password) :密码散列值和用户输入的密码是
        return check_password_hash(self.password_hash, password)

    # def generate_confirmation_token(self, expire=3600):
    #     """生成一个令牌,有效期默认为一小时。"""
    #     # secret_key = "westos"
    #     s = TimedJSONWebSignatureSerializer(current_app.config['SECRET_KEY'], expire)
    #     return s.dumps({'confirm': self.id})

    # def confirm(self, token):
    #     """
    #     http://127.0.0.1:8000/auth/confirm/hdhewufdiheryiufhyruiiiiiiigyuhgh
    #     :param token:
    #     :return:
    #     """
    #     s = TimedJSONWebSignatureSerializer(current_app.config['SECRET_KEY'])
    #     try:
    #         data = s.loads(token)  # {'confirm': 1}
    #     except Exception as e:
    #         return False
    #     else:
    #         self.confirmed = True
    #         db.session.add(self)
    #         db.session.commit()
    #         return True

    # def ping(self):
    #     """刷新用户的最后访问时间"""
    #     self.last_seen = datetime.utcnow()
    #     db.session.add(self)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    

    # @staticmethod
    # def get_user(username):
    #     return User.query.filter(User.username == username).first()

    # @staticmethod
    # def authenticate(username, password):
    #     flag_user_exist = True
    #     flag_password_correct = True

    #     user = User.query.filter(User.username == username).first()
    #     if user and user.active == 1:
    #         if not user.password == password:
    #             flag_password_correct = False
    #     else:
    #         flag_user_exist = False

    #     return flag_user_exist, flag_password_correct, user

    # @staticmethod
    # def get_users():
    #     return User.query.filter(User.active == 1).all()

    # @staticmethod
    # def insert_user(user):
    #     db.session.add(user)
    #     db.session.commit()

    # @staticmethod
    # def update_user():
    #     db.session.commit()

    # @staticmethod
    # def deactivate_user():
    #     db.session.commit()

    def __repr__(self):
        return "<User: %s>" % (self.username)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    # 做了两件事情: 1). Role添加属性users    2). User添加属性role
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return "<Role: %s>" % (self.name)
