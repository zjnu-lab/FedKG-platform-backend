from dis import code_info
from models.user import User
# from models.new_entity import NewEntity
from models.task import Task
from service import user_service
from utils.code import StatusCode

class TaskService(object):
    
    def __init__(self):
        pass

    def create_new_task(self, username,task_attributes=None):
        '''创建新的训练任务

        :username: 用户名字
        :task_attribute: 新任务的相关信息
        :return: StatusCode
        '''

        code,user = user_service.find_user(username)

        if user is None:
            return code

        task = Task(user_id = user.id, task_attributes = task_attributes)
                
        task.save_to_db() 

        return StatusCode.OK

    def get_user_tasks(self,username):
        '''获取用户创建的任务

        :username: 用户名字
        :return: StatusCode
        '''
        code,user = user_service.find_user(username)

        if user is None:
            return code,None

    
        user_tasks = user.user_tasks
       

        return StatusCode.OK,user_tasks

    def get_all_tasks(self):
        return StatusCode.OK,Task.query.all()

    def get_task_by_id(self,task_id):
        return StatusCode.OK,Task.query.filter(Task.id == task_id).first()

    # def get_tasks_status(self,status=None):
    #     '''根据status获取任务

    #     :status: 任务的状态，为空时 返回所有状态的任务
    #     :return: StatusCode,任务list
    #     '''
    #     if status is None:
    #         return StatusCode.OK, self.get_all_tasks()
    #     return StatusCode.OK, Task.query.filter(Task.status == status).all()

    def get_task(self,username,task_id):
        
        '''用户获取具体某一个任务

        :username: 用户名字
        :task_id:任务的id
        :return: StatusCode,任务
        '''
        
        task = Task.query.filter(Task.id == task_id).first()
        if task is None:
            return StatusCode.NWENETITY_NOTEXIST,None
        user = user_service.find_user_by_id(task.task_user_id)

        if username != user.username:
            return StatusCode.GETNWENTITY_FAILED,None
        else:
            return StatusCode.OK,task
        # return StatusCode.GETNWENTITY_SUCCESS,task


    def delete_task(self,username,task_id):

        '''用户删除具体某一个任务

        :username: 用户名字
        :new_entity_id: 任务的id
        :return: StatusCode
        '''

        code,task = self.get_task(username,task_id)
        if task is None:
            return code
        else:
            task.delete_from_db()
            return StatusCode.OK

        
    

    def edit_task(self,username,task_id,task_attributes):

        '''用户修改具体某一个任务

        :username: 用户名字
        :task_id: 任务的id
        :task_attribute: 修改后的任务属性
        :return: StatusCode
        '''

        code,task= self.get_task(username,task_id)
        if task is None:
            return code
        else:

            
            # task.status = task_attributes.get('status')
            task.task_name = task_attributes.get('task_name')
            task.task_summary = task_attributes.get('task_summary')
            task.task_intro = task_attributes.get('task_intro')
            task.server_ip = task_attributes.get('server_ip')
            task.server_port = task_attributes.get('server_port')
            task.client_code_url = task_attributes.get('client_code_url')

            task.save_to_db()

            return StatusCode.OK
   