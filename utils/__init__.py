from flask import jsonify

#统一返回方法
def response(http_code,code=None,message=None,data=None):
    
    return jsonify({
            "http_code": http_code,
            "code": code,
            "message": message,
            "data": data
        })
