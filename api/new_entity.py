
from ast import Is
from curses import use_default_colors
from email.errors import StartBoundaryNotFoundDefect
import resource
from tempfile import TemporaryDirectory
from flask_restful import Resource, reqparse
from flask_jwt_extended import get_jwt_identity,jwt_required

from utils import response
from utils.code import StatusCode
from service import new_entity_service,user_service


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
            .add_argument('newentity', type = dict, required = True) \
            .parse_args()


        # 序列化 待测试是否能传入blob 字段
        blob = new_entity_serialize(dict(args.get('newentity')))

        # 序列化结果传入参数 BLOB
        flag = new_entity_service.create_new_entity(username,blob)

        if flag == False:
            return response(200,StatusCode.UPNWENTITY_FAILED.code,StatusCode.UPNWENTITY_FAILED.message)
        else:
            return response(200,StatusCode.UPNWENTITY_SUCCESS.code,StatusCode.UPNWENTITY_SUCCESS.message)
    
    
    @jwt_required()
    def get(self):
        args = reqparse.RequestParser() \
            .add_argument('newentity_id', type=int, location='args',required = True) \
            .parse_args()

        newent_id = args["newentity_id"]

        username = get_jwt_identity()


        #传入 用户名，以及新实体id 
        flag,new_entity = new_entity_service.get_new_entity(username,newent_id)

        if flag == False:
            return response(400,StatusCode.GETNWENTITY_FAILED.code,StatusCode.GETNWENTITY_FAILED.message)
        else:
            entity_attributes = new_entity.entity_attributes

            entity_attributes = new_entity_deserialize(entity_attributes)
            
            print(entity_attributes)

            data = {
                "newent_id": new_entity.id,
                "time": new_entity.create_time,
                "status": new_entity.status,
                "entity_info": entity_attributes,  
                "failed_reason": new_entity.failed_reason
            }

            return response(200,StatusCode.GETNWENTITY_SUCCESS.code,StatusCode.GETNWENTITY_SUCCESS.message,data)


        # 需要确定返回的data，上传时间，审核状态，
        

    @jwt_required()
    def put(self):
        args = reqparse.RequestParser() \
            .add_argument('newentity_id', type=int, location='args',required = True) \
            .add_argument('new_attribute', type = dict, required = True) \
            .parse_args()
        
        username = get_jwt_identity()

        nwent_id = args["newentity_id"]

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
            .add_argument('newentity_id', type=int, location='args',required = True) \
            .parse_args()

        username = get_jwt_identity()

        nwent_id = args["newentity_id"]

        flag = new_entity_service.delete_new_entity(username,nwent_id)

        if flag == False:
            return response(400,StatusCode.EDITNWENTITY_FAILED.code,StatusCode.EDITNWENTITY_FAILED.message)
        else:
            return response(200, StatusCode.OK.code, StatusCode.OK.message)


class UserNewEntities(Resource):

    @jwt_required()
    def get(self):

        username = get_jwt_identity()

        # status 新实体审核状态，默认为空，则返回用户所有新实体
        args = reqparse.RequestParser() \
            .add_argument('status', type=int, location='args') \
            .parse_args()

        status = args.get('status',None)


        new_entities_list = new_entity_service.get_user_new_entities(username,status)
        

        # for i in new_entities:
        #     print(i.create_time)

        # print(list(new_entities))

        # return response(200, StatusCode.OK.code, StatusCode.OK.message)

        entities_list = []

        for newent in new_entities_list:

            newent_attributes = new_entity_deserialize(newent.entity_attributes)

            temp = {
                "newent_id":newent.id,
                "newent_name":newent_attributes.get("newentity_name"),
                "newent_status":newent.status,
            }
            
            entities_list.append(temp)
            
        data = {
            "entities_list":entities_list,
        }

        return response(200, StatusCode.OK.code, StatusCode.OK.message,data)



        # 修改 




class Review(Resource):
    
    @jwt_required()
    def post(self):
        # 审核新实体

        username = get_jwt_identity()

        # 需要做一个是否是管理员的判断（todo）
        #

        is_admin = user_service.is_admin(username)
        if not is_admin:
            return response(400,StatusCode.USER_ERR.code,StatusCode.USER_ERR.message) 

        args = reqparse.RequestParser() \
            .add_argument('review_info', type=dict, required=True, nullable = False) \
            .parse_args()
            # .add_argument("status", type=int, location='dict', required=True, nullable = False ) \
            

        # nwent_id = args["nwentity_id"] 
        # status = args["status"]
        review_info = args.get("review_info")
        # 获取待审核的实体id 列表
        review_entities_list = review_info.get("entities_list")
        # 获取审核的状态
        review_status = review_info.get("status")

        flag = new_entity_service.review_new_entities(review_entities_list,review_status)
        
        if flag == False:
            return response(400,StatusCode.REVIEWNWENTITY_FAILED,StatusCode.REVIEWNWENTITY_FAILED.message)
        else:
            return response(200, StatusCode.REVIEWNWENTITY_SUCCESS.code, StatusCode.REVIEWNWENTITY_SUCCESS.message)
 
        # 修改 


        

    @jwt_required()
    def get(self):
        # 获取待审核的新实体

        username = get_jwt_identity()
        # 根据状态返回 0: 未审核，1: 审核通过未提交， 2: 审核不通过，3： 已提交
        args = reqparse.RequestParser() \
            .add_argument('status', type=int, location="args") \
            .parse_args()

        status = args.get('status', None)
        


        is_admin = user_service.is_admin(username)

        if not is_admin:
            return response(400,StatusCode.ADMIN_ERR.code,StatusCode.ADMIN_ERR.message)
        
        new_entities_list = new_entity_service.get_review_entities(status)

        
        entities_list = []

        for newent in new_entities_list:

            newent_attributes = new_entity_deserialize(newent.entity_attributes)

            temp = {
                "newent_id":newent.id,
                "newent_name":newent_attributes.get("newentity_name"),
                "newent_status":newent.status,
            }
            
            entities_list.append(temp)
            
        data = {
            "entities_list":entities_list,
        }
            
        return response(200,StatusCode.OK.code,StatusCode.OK.message,data)



