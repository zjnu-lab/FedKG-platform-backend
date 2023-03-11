
from ast import Is
from curses import use_default_colors
from email.errors import StartBoundaryNotFoundDefect
import resource
from tempfile import TemporaryDirectory
from flask_restful import Resource, reqparse
from flask_jwt_extended import get_jwt_identity,jwt_required

from utils import response
from utils.code import StatusCode
from service import model_service,user_service


from utils import response,new_entity_serialize,new_entity_deserialize
from utils.code import StatusCode

import pickle


class Model(Resource):

    #创建新的模型
    @jwt_required()
    def post(self):


        username = get_jwt_identity()

        args = reqparse.RequestParser() \
            .add_argument('model_attributes', type = dict, required = True) \
            .parse_args()
        model_attributes = args['model_attributes']
        # print(model_attributes)
        #创建新模型
        code = model_service.create_new_model(username,model_attributes)

        if code == StatusCode.OK:
            return response(200,code.code,code.message)
        else:
            return response(400,code.code,code.message)
    
    
    @jwt_required()
    def get(self):
        args = reqparse.RequestParser() \
            .add_argument('model_id', type=int, location='json') \
            .add_argument('model_name', type=int, location='json') \
            .parse_args()

        model_id = args.get("model_id",None)
        model_name = args.get("model_name",None)
        

        username = get_jwt_identity()

        code = None
        #传入 用户名，以及任务id 
        if model_id is not None:
            code,model = model_service.get_model_by_id(model_id)
        elif model_name is  not None:
            code,model = model_service.get_model_by_name(model_name)

        if code == StatusCode.OK:
            # entity_attributes = task.task_attributes
            # print(entity_attributes)

            data = {
                "model_id" : model.id,
                "create_time" : model.create_time,
                "model_name" : model.model_name,
                "model_desc" : model.model_desc,
                "client_code" : model.client_code,
                "server_code" : model.server_code
            }
            
            return response(200,code.code,code.message,data)
        else:
            return response(400,code.code,code.message)

        # 需要确定返回的data，上传时间，审核状态，
        

    @jwt_required()
    def put(self):
        args = reqparse.RequestParser() \
            .add_argument('model_id', type=int, location='json',required = True) \
            .add_argument('model_attributes', type = dict,location='json', required = True) \
            .parse_args()
        
        username = get_jwt_identity()

        model_id = args["model_id"]
        # print(nwent_id)

        model_attributes = args["model_attributes"]

        # new_attribute = new_entity_serialize(dict(new_attribute))


        code = model_service.edit_model(username,model_id, model_attributes)
        
        if code == StatusCode.OK:
            return response(200,code.code,code.message)
        else:
            return response(400,code.code,code.message)

    @jwt_required()
    def delete(self):
        args = reqparse.RequestParser() \
            .add_argument('model_id', type=int, location='json',required = True) \
            .parse_args()

        username = get_jwt_identity()

        model_id = args["model_id"]

        code = model_service.delete_model(username,model_id)

        if code == StatusCode.OK:
            return response(200,code.code,code.message)
        else:
            return response(400, code.code, code.message)

class Models(Resource):

    @jwt_required()
    def get(self):

        # args = reqparse.RequestParser() \
        #     .add_argument('status', type=int, location='json') \
        #     .parse_args()

        username = get_jwt_identity()

        # status = args.get('status', None)

        code, models_list = model_service.get_all_model()

        if code == StatusCode.OK:

            data_list = []

            for model in models_list:

                # newent_attributes = new_entity_deserialize(newent.entity_attributes)

                temp = {
                    "id" : model.id,
                    "create_time" : model.create_time,
                    "model_name" : model.model_name,
                    "model_desc": model.model_desc,
                    "server_code" : model.server_code,
                    "client_code" :model.client_code
                }
                
                data_list.append(temp)
                
            data = {
                "model_list":data_list,
            }
            print(data)

            return response(200, code.code,code.message,data)
        else:
            return response(400, code.code,code.message)



class UserModels(Resource):

    @jwt_required()
    def get(self):

        username = get_jwt_identity()

    
        # args = reqparse.RequestParser() \
        #     .add_argument('status', type=int, location='json') \
        #     .parse_args()

        # status = args.get('status',None)


        code,models_list = model_service.get_user_models(username)
        
        if code == StatusCode.OK:

            data_list = []

            for model in models_list:

                temp = {
                    "id" : model.id,
                    "create_time" : model.create_time,
                    "model_name" : model.model_name,
                    "model_desc": model.model_desc,
                    "server_code" : model.server_code,
                    "client_code" :model.client_code,
                }
                
                data_list.append(temp)
                

                
            data = {
                "model_list":data_list,
            }

            return response(200, code.code,code.message,data)
        else:
            return response(400, code.code,code.message)


        # 修改 




