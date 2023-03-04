from contextlib import nullcontext
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
# from app import db, login_manager
# from flask_login import UserMixin
# from itsdangerous import TimedJSONWebSignatureSerializer
from datetime import datetime

# Flask中一个Model子类就是数据库中的一个表。默认表名'User'.lower() ===> user

class Model(db.Model):

    __tablename__ = 'model'  # 自定义数据表的表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    # status 标识 审核状态 0: 未审核，1: 审核通过未同步， 2: 审核不通过，3： 已同步
    # status = db.Column(db.Integer,default=0,nullable=False)

    model_name = db.Column(db.String(200),nullable=False)
    model_desc = db.Column(db.Text,nullable=True)
    
    server_code = db.Column(db.String(400),nullable=False)
    client_code = db.Column(db.String(400),nullable=False)

    # 外键关联
    model_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    model_user = db.relationship("User",backref="user_model",foreign_keys=[model_user_id])
    

    # upload_user = db.relationship("Users",back_populates="new_entities")
    # review_user = db.relationship("Users",back_populates="new_entities")


    def __init__(self, user_id=None,model_attributes=None):
        
        self.model_user_id = user_id
        self.model_name = model_attributes.get('model_name')
        self.model_desc = model_attributes.get('model_desc')
        self.client_code = model_attributes.get('client_code')
        self.server_code = model_attributes.get('server_code')
        

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()




