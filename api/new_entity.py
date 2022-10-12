
from curses import use_default_colors
from email.errors import StartBoundaryNotFoundDefect
import resource
from flask_restful import Resource, reqparse
from flask_jwt_extended import get_jwt_identity,jwt_required

from utils import response
from utils.code import StatusCode
from service import new_entity_service


from utils import response,new_entity_serialize,new_entity_deserialize
from utils.code import StatusCode

import pickle


class NewEntity(Resource):

    #创建新的实体
    @jwt_required()
    def post(self):


        username = get_jwt_identity()

        # args 解析 -> 序列化
        
        args = reqparse.RequestParser() \
            .add_argument('attribute', type = dict, required = True) \
            .parse_args()


        # 序列化 待测试是否能传入blob 字段
        blob = new_entity_serialize(dict(args))

        # 序列化结果传入参数 BLOB
        flag = new_entity_service.create_new_entity(username,blob)

        if flag == False:
            return response(200,StatusCode.UPNWENTITY_FAILED.code,StatusCode.UPNWENTITY_FAILED.message)
        else:
            return response(200,StatusCode.UPNWENTITY_SUCCESS.code,StatusCode.UPNWENTITY_SUCCESS.message)
    
    
    @jwt_required()
    def get(self):
        args = reqparse.RequestParser() \
            .add_argument('nwentity_id', type=int, location='args',required = True) \
            .parse_args()

        nwent_id = args["nwentity_id"]

        username = get_jwt_identity()


        #传入 用户名，以及新实体id 
        flag,new_entity = new_entity_service.get_new_entity(username,nwent_id)

        if flag == False:
            return response(400,StatusCode.GETNWENTITY_FAILED.code,StatusCode.GETNWENTITY_FAILED.message)
        else:
            entity_attributes = new_entity.entity_attributes

            entity_attributes = new_entity_deserialize(entity_attributes)

            data = {
                "nwent_id": new_entity.id,
                "time": new_entity.create_time,
                "status": new_entity.status,
                "attribute": entity_attributes,  
                "failed_reason": new_entity.failed_reason
            }

            return response(200,StatusCode.GETNWENTITY_SUCCESS.code,StatusCode.GETNWENTITY_SUCCESS.message,data)


        # 需要确定返回的data，上传时间，审核状态，
        

    @jwt_required()
    def put(self):
        args = reqparse.RequestParser() \
            .add_argument('nwentity_id', type=int, location='args',required = True) \
            .add_argument('new_attribute', type = dict, required = True) \
            .parse_args()
        
        username = get_jwt_identity()

        nwent_id = args["nwentity_id"]

        new_attribute = args["new_attribute"]

        new_attribute = new_entity_serialize(dict(new_attribute))


        flag = new_entity_service.edit_new_entity(username,nwent_id, new_attribute)
        
        if flag == False:
            return response(400,StatusCode.EDITNWENTITY_FAILED,StatusCode.EDITNWENTITY_FAILED.message)
        else:
            return response(200,StatusCode.EDITNWENTITY_SUCCESS.code,StatusCode.EDITNWENTITY_SUCCESS.message)

    @jwt_required()
    def delete(self):
        args = reqparse.RequestParser() \
            .add_argument('nwentity_id', type=int, location='args',required = True) \
            .parse_args()

        username = get_jwt_identity()

        nwent_id = args["nwentity_id"]

        flag = new_entity_service.delete_new_entity(username,nwent_id)

        if flag == False:
            return response(400,StatusCode.EDITNWENTITY_FAILED.code,StatusCode.EDITNWENTITY_FAILED.message)
        else:
            return response(200, StatusCode.OK.code, StatusCode.OK.message)


class UserNewEntities(Resource):

    @jwt_required()
    def get(self):

        # 表单参数 nwentity_id,以及新的属性表格
        username = get_jwt_identity()

        new_entities = new_entity_service.get_user_new_entities(username)
        
        for i in new_entities:
            print(i.create_time)

        print(list(new_entities))

        return response(200, StatusCode.OK.code, StatusCode.OK.message)

        pass



        # 修改 




class Review(Resource):
    
    @jwt_required()
    def post(self):

        username = get_jwt_identity()

        # 需要做一个是否是管理员的判断（todo）
        # 
        args = reqparse.RequestParser() \
            .add_argument('nwentity_id', type=int, location='form', required=True, nullable = False) \
            .add_argument("status", type=int, location='form', required=True, nullable = False ) \
            .parse_args()

        nwent_id = args["nwentity_id"] 
        status = args["status"]


        flag = new_entity_service.review_new_entity(nwent_id,status)
        
        if flag == False:
            return response(400,StatusCode.EDITNWENTITY_FAILED.code,StatusCode.EDITNWENTITY_FAILED.message)
        else:
            return response(200, StatusCode.OK.code, StatusCode.OK.message)
 
        # 修改 


        

    
    def get(self):
        pass

