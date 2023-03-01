from contextlib import nullcontext
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
# from app import db, login_manager
# from flask_login import UserMixin
# from itsdangerous import TimedJSONWebSignatureSerializer
from datetime import datetime

# Flask中一个Model子类就是数据库中的一个表。默认表名'User'.lower() ===> user

class Task(db.Model):

    __tablename__ = 'task'  # 自定义数据表的表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    # status 标识 审核状态 0: 未审核，1: 审核通过未同步， 2: 审核不通过，3： 已同步
    status = db.Column(db.Integer,default=0,nullable=False)

    task_name = db.Column(db.String(200),nullable=False)
    task_summary = db.Column(db.String(200),nullable=False)
    task_intro = db.Column(db.Text,nullable=True)
    server_ip = db.Column(db.String(100),nullable=False)
    server_port = db.Column(db.String(100),nullable=False)
    client_code_url = db.Column(db.String(200),nullable=False)

    
#     `id` INT UNSIGNED AUTO_INCREMENT,
#    `create_time` VARCHAR(100) NOT NULL,
#    `status` INT UNSIGNED default 0 NOT NULL,
#    `task_name` VARCHAR(200) NOT NULL,
#    `server_ip` VARCHAR(100) NOT NULL,
#    `server_port` VARCHAR(100) NOT NULL,
#    `task_intro` TEXT,
#    `client_code_url` VARCHAR(200) NOT NULL,
#    `task_user_id` INT UNSIGNED,
#    PRIMARY KEY ( `id` )
    

    # 外键关联
    task_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    task_user = db.relationship("User",backref="user_tasks",foreign_keys=[task_user_id])
    

    # upload_user = db.relationship("Users",back_populates="new_entities")
    # review_user = db.relationship("Users",back_populates="new_entities")


    def __init__(self, user_id=None,task_attributes=None):
        
        self.task_user_id = user_id
        self.status = 0
        self.task_name = task_attributes.get('task_name')
        self.task_summary = task_attributes.get('task_summary')
        self.task_intro = task_attributes.get('task_intro')
        self.server_ip = task_attributes.get('server_ip')
        self.server_port = task_attributes.get('server_port')
        self.client_code_url = task_attributes.get('client_code_url')
        

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()




