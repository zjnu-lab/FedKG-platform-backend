
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

    # 上传新实体模块
    UPNWENTITY_SUCCESS = (2000, '上传新实体成功')
    UPNWENTITY_FAILED = (2001, '上传新实体失败')
    GETNWENTITY_SUCCESS = (2002,'获取成功')
    GETNWENTITY_FAILED = (2003,'不是实体上传者，获取失败')
    EDITNWENTITY_SUCCESS = (2004,'修改成功')
    EDITNWENTITY_FAILED = (2005,'不是实体上传者，不能修改')
    DELNENTITY_SUCCESS = (2006,'删除成功')
    DELNWENTITY_FAILED = (2007,'不是实体上传者，不能删除')



    @property
    def code(self):
        """获取状态码""" 
        return self.value[0]

    @property
    def message(self):
        """获取状态码信息"""
        return self.value[1]