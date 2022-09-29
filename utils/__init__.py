from flask import jsonify

#统一返回方法
def response(httpcode,code="",message="",data=""):
    
    resp = jsonify({
            "code": code,
            "message": message,
            "data": data
        })
    resp.status_code = httpcode
    return resp
