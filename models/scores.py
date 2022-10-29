from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
# from app import db, login_manager
# from flask_login import UserMixin
# from itsdangerous import TimedJSONWebSignatureSerializer
from datetime import datetime


class Scores(db.Model):

    __tablename__ = 'scores'  # 自定义数据表的表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    # 积分变动原因/事件,e.g 用户添加了实体
    change_reasons = db.Column(db.Text)
    # 积分变动记录 e.g.“+1”
    change_records = db.Column(db.Text)
    # 外键关联
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # user = db.relationship("User",backref="score_records",foreign_keys=[user_id])
    
    # upload_user = db.relationship("Users",back_populates="new_entities")
    # review_user = db.relationship("Users",back_populates="new_entities")


    def __init__(self, user_id,change_reasons,change_records):
        
        self.user_id = user_id
        self.change_records = change_records
        self.change_reasons = change_reasons


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()




