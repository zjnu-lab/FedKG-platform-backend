from dis import code_info
from models.user import User
from models.new_entity import NewEntity
from service import user_service
from utils.code import StatusCode

class NewEntityService(object):
    
    def __init__(self):
        pass

    def create_new_entity(self, username,attribute_blob=None):

        code,user = user_service.find_user(username)

        if user is None:
            return code

        new_entity = NewEntity(user_id = user.id, entity_attributes = attribute_blob)
                
        new_entity.save_to_db() 

        return StatusCode.UPNWENTITY_SUCCESS

    def get_user_new_entities(self,username,status=None):
        code,user = user_service.find_user(username)

        if user is None:
            return code,None

        if status is None:
            user_new_entities = user.upload_new_entities
        else:
            user_new_entities = NewEntity.query.filter(NewEntity.upload_user_id == user.id,NewEntity.status == status).all()

        return StatusCode.OK,user_new_entities

    def get_all_new_entities(self):
        return NewEntity.query.all()

    def get_entity_by_id(self,nwe_entity_id):
        return NewEntity.query.filter(NewEntity.id == nwe_entity_id).first()

    def get_review_entities(self,status=None):
        if status is None:
            return StatusCode.OK, self.get_all_new_entities()
        return StatusCode.OK, NewEntity.query.filter(NewEntity.status == status).all()

    def get_new_entity(self,username,new_entity_id):
        
        newent = NewEntity.query.filter(NewEntity.id == new_entity_id).first()
        if newent is None:
            return StatusCode.NWENETITY_NOTEXIST,None
        user = user_service.find_user_by_id(newent.upload_user_id)

        if username != user.username:
            return StatusCode.GETNWENTITY_FAILED,None
        else:
            return StatusCode.GETNWENTITY_SUCCESS,newent


    def delete_new_entity(self,username,new_entity_id):

        code,newent = self.get_new_entity(username,new_entity_id)
        if newent is None:
            return code
        else:
            newent.delete_from_db()
            return StatusCode.DELNENTITY_SUCCESS

        
    

    def edit_new_entity(self,username,new_entity_id,new_attribute):

        code,newent= self.get_new_entity(username,new_entity_id)
        if newent is None:
            return code
        else:
            newent.entity_attributes = new_attribute

            newent.save_to_db()

            return StatusCode.EDITNWENTITY_SUCCESS

    def review_new_entities(self,review_entities_list,review_status):


        for newent_id in review_entities_list:


            newent = self.get_entity_by_id(newent_id)

            # 做一个状态判断，重复状态不操作，设置为0 不操作 ，因为已经审核过，不能为0
            if review_status == 0 or newent.status == review_status:
                continue

            newent.status = review_status

            newent.save_to_db()

        return StatusCode.REVIEWNWENTITY_SUCCESS