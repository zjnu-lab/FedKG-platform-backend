
from ast import Is
from curses import use_default_colors
from email.errors import StartBoundaryNotFoundDefect
import resource
from tempfile import TemporaryDirectory
from flask_restful import Resource, reqparse
from flask_jwt_extended import get_jwt_identity,jwt_required

from utils import response
from utils.code import StatusCode
from service import task_service,user_service


from utils import response,new_entity_serialize,new_entity_deserialize
from utils.code import StatusCode

import pickle


class Task(Resource):

    #创建新的任务
    @jwt_required()
    def post(self):


        username = get_jwt_identity()

        args = reqparse.RequestParser() \
            .add_argument('task_attributes', type = dict, required = True) \
            .parse_args()
        task_attributes = args['task_attributes']
        # print(task_attributes)
        #创建新任务
        code = task_service.create_new_task(username,task_attributes)

        if code == StatusCode.OK:
            return response(200,code.code,code.message)
        else:
            return response(400,code.code,code.message)
    
    
    @jwt_required()
    def get(self):
        args = reqparse.RequestParser() \
            .add_argument('task_id', type=int,location='args',required = True) \
            .parse_args()

        task_id = args["task_id"]

        username = get_jwt_identity()


        #传入 用户名，以及任务id 
        code,task = task_service.get_task_by_id(task_id)

        if code == StatusCode.OK:
            # entity_attributes = task.task_attributes
            # print(entity_attributes)

            data = {
                "id" : task.id,
                "create_time" : task.create_time,
                
                "task_status" : task.task_status,
                "task_name" : task.task_name,
                "task_desc" : task.task_desc,
                "server_ip" : task.server_ip,
                "server_port" : task.server_port,
                "task_model" : task.task_model,
                "task_rounds": task.task_rounds,
                "task_log":task.task_log,
            }
            
            return response(200,code.code,code.message,data)
        else:
            return response(400,code.code,code.message)

        # 需要确定返回的data，上传时间，审核状态，
        

    @jwt_required()
    def put(self):
        args = reqparse.RequestParser() \
            .add_argument('task_id', type=int, location='json',required = True) \
            .add_argument('task_attributes', type = dict,location='json', required = True) \
            .parse_args()
        
        username = get_jwt_identity()

        task_id = args["task_id"]
        # print(nwent_id)

        task_attributes = args["task_attributes"]

        # new_attribute = new_entity_serialize(dict(new_attribute))


        code = task_service.edit_task(username,task_id, task_attributes)
        
        if code == StatusCode.OK:
            return response(200,code.code,code.message)
        else:
            return response(400,code.code,code.message)

    @jwt_required()
    def delete(self):
        args = reqparse.RequestParser() \
            .add_argument('task_id', type=int, location='json',required = True) \
            .parse_args()

        username = get_jwt_identity()

        task_id = args["task_id"]

        code = task_service.delete_task(username,task_id)

        if code == StatusCode.OK:
            return response(200,code.code,code.message)
        else:
            return response(400, code.code, code.message)

class Tasks(Resource):

    @jwt_required()
    def get(self):

    

        username = get_jwt_identity()

        # status = args.get('status', None)
        code,tasks_list = task_service.get_all_tasks()

        if code == StatusCode.OK:

            data_list = []

            for task in tasks_list:

                # newent_attributes = new_entity_deserialize(newent.entity_attributes)

                temp = {
                    "id" : task.id,
                    "create_time" : task.create_time,
                    "task_status" : task.status,
                    "task_name" : task.task_name,
                    "task_desc" : task.task_desc,

                    "server_ip" : task.server_ip,
                    "server_port" : task.server_port,
                    "task_model" : task.task_model,
                    "task_rounds": task.task_rounds,
                }
                
                data_list.append(temp)
                
            data = {
                "task_list":data_list,
            }
            print(data)

            return response(200, code.code,code.message,data)
        else:
            return response(400, code.code,code.message)



class UserTasks(Resource):

    @jwt_required()
    def get(self):

        username = get_jwt_identity()

      


        code,tasks_list = task_service.get_user_tasks(username)
        
        if code == StatusCode.OK:

            data_list = []

            for task in tasks_list:

                temp = {
                    "task_id" : task.id,
                    "create_time" : task.create_time,
                    "task_status" : task.task_status,
                    "task_name" : task.task_name,
                    "task_desc" : task.task_desc,
                    "server_ip" : task.server_ip,
                    "server_port" : task.server_port,
                    "task_model" : task.task_model,
                    "task_rounds" : task.task_rounds,
                }
                
                data_list.append(temp)
                

                
            data = {
                "task_list":data_list,
            }

            return response(200, code.code,code.message,data)
        else:
            return response(400, code.code,code.message)


        # 修改 




