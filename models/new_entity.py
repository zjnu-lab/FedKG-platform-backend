from contextlib import nullcontext
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
# from app import db, login_manager
# from flask_login import UserMixin
# from itsdangerous import TimedJSONWebSignatureSerializer
from datetime import datetime

# Flask中一个Model子类就是数据库中的一个表。默认表名'User'.lower() ===> user

class NewEntity(db.Model):

    __tablename__ = 'new_entities'  # 自定义数据表的表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    # status 标识 审核状态 0: 未审核，1: 审核通过， 2: 审核不通过，3： 未提交,4:提交
    status = db.Column(db.Integer,default=0,nullable=False)
    failed_reason = db.Column(db.Text,nullable=True)

    entity_attributes = db.Column(db.LargeBinary)
    

    # 外键关联
    upload_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    review_user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=True)

    upload_user = db.relationship("User",backref="upload_new_entities",foreign_keys=[upload_user_id])
    review_user = db.relationship("User",backref="review_new_entities",foreign_keys=[review_user_id])

    # upload_user = db.relationship("Users",back_populates="new_entities")
    # review_user = db.relationship("Users",back_populates="new_entities")


    def __init__(self, user_id=None,entity_attributes = None):
        
        self.upload_user_id = user_id
        self.entity_attributes = entity_attributes


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()




