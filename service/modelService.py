from dis import code_info
from models.user import User
# from models.new_entity import NewEntity
from models.model import Model
from service import user_service
from utils.code import StatusCode

class ModelService(object):
    
    def __init__(self):
        pass

    def create_new_model(self, username,model_attributes=None):
        '''创建新的训练模型

        :username: 用户名字
        :model_attribute: 新模型的相关信息
        :return: StatusCode
        '''

        code,user = user_service.find_user(username)

        if user is None:
            return code

        model = Model(user_id = user.id, model_attributes = model_attributes)
                
        model.save_to_db() 

        return StatusCode.OK

    def get_user_models(self,username):
        '''获取用户创建的模型

        :username: 用户名字
        :return: StatusCode
        '''
        code,user = user_service.find_user(username)

        if user is None:
            return code,None

        
        user_models = user.user_models
        
        return StatusCode.OK,user_models

    def get_all_model(self):
        return StatusCode.OK,Model.query.all()

    def get_model_by_id(self,model_id):
        return StatusCode.OK,Model.query.filter(Model.id == model_id).first()


    def get_model(self,username,model_id):
        
        '''用户获取具体某一个任务

        :username: 用户名字
        :task_id:任务的id
        :return: StatusCode,任务
        '''
        
        model = Model.query.filter(Model.id == model_id).first()
        if model is None:
            return StatusCode.NWENETITY_NOTEXIST,None
        user = user_service.find_user_by_id(model.model_user_id)

        if username != user.username:
            return StatusCode.GETNWENTITY_FAILED,None
        else:
            return StatusCode.OK,model
        # return StatusCode.GETNWENTITY_SUCCESS,task


    def delete_model(self,username,model_id):

        '''用户删除具体某一个模型

        :username: 用户名字
        :new_entity_id: 模型的id
        :return: StatusCode
        '''

        code,model = self.get_task(username,model_id)
        if model is None:
            return code
        else:
            model.delete_from_db()
            return StatusCode.OK

        
    

    def edit_model(self,username,model_id,model_attributes):

        '''用户修改具体某一个模型

        :username: 用户名字
        :task_id: 模型的id
        :task_attribute: 修改后的模型属性
        :return: StatusCode
        '''

        code,model= self.get_model(username,model_id)
        if model is None:
            return code
        else:

            
            # task.status = task_attributes.get('status')
            model.model_name = model_attributes.get('model_name')
            model.model_desc = model_attributes.get('model_desc')
            model.server_code = model_attributes.get('server_code')
            model.client_code = model_attributes.get('client_code')

            model.save_to_db()

            return StatusCode.OK
   