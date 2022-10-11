from models.new_entity import NewEntity
from service import user_service

class NewEntityService(object):
    
    def __init__(self):
        pass

    def create_new_entity(self, username,attribute_blob=None):
        is_success = False
        

        user = user_service.get_user(username)

        new_entity = NewEntity(user_id = user.id, entity_attributes = attribute_blob)

        # # 序列化 args
        # #todo
        # new_entity.entity_attributes =attribute_blob
        
        
        new_entity.save_to_db()
        is_success = True
        
        return is_success

    def get_user_new_entities(self,username):
        user = user_service.get_user(username)

        user_new_entities = user.new_entities

        return user_new_entities

    def get_all_new_entities(self):
        return NewEntity.query.all()

    def get_new_entitit(self,new_entity_id):

        return NewEntity.query.filter(NewEntity.id == new_entity_id).first()

    def delete_new_entity(self,new_entity_id):

        new_entity = self.get_new_entitit(new_entity_id)

        new_entity.delete_from_db()

    def review_new_entity(self,new_entity_id,status):
        pass

    def edit_new_entity(self,new_entity_id,new_attribute):

        new_entity = self.get_new_entity(new_entity_id)

        new_entity.entity_attributes = new_attribute

        new_entity.save_to_db()
        
        pass