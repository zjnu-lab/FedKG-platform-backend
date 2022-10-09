
from flask_restful import Resource, reqparse
from flask_jwt_extended import get_jwt_identity,jwt_required

from utils import response
from utils.code import StatusCode
from service import new_entity_service


from utils import response,new_entity_serialize,new_entity_deserialize
from utils.code import StatusCode

class NewEntity(Resource):

    #创建新的实体
    @jwt_required()
    def post(self):


        username = get_jwt_identity()

        # args 解析 -> 序列化
        
        args = reqparse.RequestParser() \
            .add_argument('attribute', type = dict, action = 'append', required = True) \
            .parse_args()


        # 序列化 待实现
        blob = new_entity_serialize(args)

        # 序列化结果传入参数 BLOB
        res = new_entity_service.create_new_entity(username,blob)


        return response(200,StatusCode.UPNWENTITY_SUCCESS.code,StatusCode.UPNWENTITY_SUCCESS.message)
    
    
    def get(self):
        pass

    def get(self,nwentity_id):
        pass
    
    def put(self,nwentity_id):
        pass

    def delete(self,nwentity_id):
        pass


class Review(Resource):
    def post(self,nwentity_id):
        pass
    
    def get(self):
        pass

