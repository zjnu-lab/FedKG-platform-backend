from flask import jsonify
import pickle
import re 
from app import jwt 
from utils.code import StatusCode
#统一返回方法
def response(httpcode,code="",message="",data=None):
    
    resp = jsonify({
            "code": code,
            "message": message,
            "data": data
        })
    resp.status_code = httpcode
    return resp

#统一序列化函数

def new_entity_serialize(args = None):
    return pickle.dumps(args)
    

def new_entity_deserialize(args = None):
    return pickle.loads(args)

# 邮箱正则识别
def validate_email(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
      return True
    else:
      return False

# token 过期处理函数
@jwt.expired_token_loader
def expired_token_callback(jwt_header,jwt_data):
    print(jwt_header)
    print(jwt_data)
    return response(401,StatusCode.TOKEN_EXPIRE.code,StatusCode.TOKEN_EXPIRE.message)