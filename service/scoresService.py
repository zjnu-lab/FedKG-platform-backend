from models.scores import Scores
from service import user_service
from utils.code import StatusCode

class ScoresService(object):
    
    def __init__(self):
        pass

    def user_scores_records(self, username):
        '''用户积分记录
        
        :username: 用户名(邮箱)
        :return: StatusCode, records list
        '''
        
        code, user = user_service.find_user(username)
        if user is None:
            return code,None

        return StatusCode.OK,user.scores_records

            
    def add_score(self,user_id,change_reason,change_score):
        pass
        
    def minus_score(self,user_id,change_reason,change_score):
        pass
        
    