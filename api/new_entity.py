
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
        res = new_entity_service.create_new_entity(username,blob)

        if res == False:
            return response(200,StatusCode.UPNWENTITY_FAILED.code,StatusCode.UPNWENTITY_FAILED.message)
        else:
            return response(200,StatusCode.UPNWENTITY_SUCCESS.code,StatusCode.UPNWENTITY_SUCCESS.message)
    
    
    @jwt_required()
    def get(self):
        args = reqparse.RequestParser() \
            .add_argument('nwentity_id', type=int, location='args',required = True) \
            .parse_args()

        nwent_id = args["nwentity_id"]

        new_entity = new_entity_service.get_entity(nwent_id)

        entity_attributes = new_entity.entity_attributes

        entity_attributes = pickle.load(entity_attributes)

        data = {
            "nwent_id": new_entity.id,
            "time": new_entity.create_time,
            "status": new_entity.status,
            "attribute": entity_attributes,  
            "failed_reason": new_entity.failed_reason
        }

        return response(200,StatusCode.OK.code,StatusCode.OK.message,data)


        # 需要确定返回的data，上传时间，审核状态，
        

    @jwt_required()
    def put(self):
        args = reqparse.RequestParser() \
            .add_argument('new_attribute', type = dict, required = True) \
            .parse_args()
        
        nwent_id = args["new_attribute"].get('nwentity_id')

        new_attribute = args["new_attribute"].get('attribute')

        new_attribute = new_entity_serialize(dict(new_attribute))


        new_entity_service.edit_new_entity(nwent_id, new_attribute)

    @jwt_required()
    def delete(self):
        args = reqparse.RequestParser() \
            .add_argument('nwentity_id', type=int, location='args',required = True) \
            .parse_args()

        nwent_id = args["nwentity_id"]

        new_entity_service.delete_new_entity(nwent_id)


class Review(Resource):
    def post(self):

        # 表单参数 nwentity_id,以及新的属性表格


        pass



        # 修改 


        

    
    def get(self):
        pass

