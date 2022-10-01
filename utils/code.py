
from enum import Enum


class StatusCode(Enum):
    """状态码枚举类"""

    OK = (0, '成功')
    ERROR = (-1, '错误')
    SERVER_ERR = (500, '服务器异常')

    # 认证模块
    RESGISTER_SUCCESS = (1000, '用户注册成功')
    USER_EXISTED = (1001, '用户已经存在')
    USER_ERR = (1002, '用户不存在')
    USER_NULL = (1003, '用户名不能为空') 
    PWD_ERR = (1004, '密码错误')
    PWD_NULL = (1005, '密码不能为空') 
    Login_SUCCESS = (1006, '登陆成功')
   
    DB_ERR = (5000, '数据错误')
    EMAIL_ERR = (5001, '邮箱错误')
    TEL_ERR = (5002, '固定电话错误')
    NODATA_ERR = (5003, '无数据')
    NEW_PWD_ERR = (5004, '新密码错误')
    OPENID_ERR = (5005, '无效的openid')
    PARAM_ERR = (5006, '参数错误')
    STOCK_ERR = (5007, '库存不足')

    @property
    def code(self):
        """获取状态码"""
        return self.value[0]

    @property
    def message(self):
        """获取状态码信息"""
        return self.value[1]