from flask import jsonify


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
    pass

def new_entity_deserialize(args = None):
    pass