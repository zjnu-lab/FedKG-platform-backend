from models.user import User
from models.new_entity import NewEntity
from service import user_service

class NewEntityService(object):
    
    def __init__(self):
        pass

    def create_new_entity(self, username,attribute_blob=None):
        is_success = False
        

        user = user_service.find_user(username)

        new_entity = NewEntity(user_id = user.id, entity_attributes = attribute_blob)
                
        new_entity.save_to_db()
        is_success = True
        
        return is_success

    def get_user_new_entities(self,username):
        user = user_service.find_user(username)

        user_new_entities = user.upload_new_entities

        return user_new_entities

    def get_all_new_entities(self):
        return NewEntity.query.all()

    def get_entity_by_id(self,nwe_entity_id):
        return NewEntity.query.filter_by(id=nwe_entity_id).first()

    def get_new_entity(self,username,new_entity_id):
        
        

        newent = NewEntity.query.filter(NewEntity.id == new_entity_id).first()
        user = user_service.find_user_by_id(newent.upload_user_id)

        if username != user.username:
            return False,None
        else:
            return True,newent


    def delete_new_entity(self,username,new_entity_id):

        flag,newent = self.get_new_entity(username,new_entity_id)
        if flag == False:
            return False
        else:
            newent.delete_from_db()
            return True

        
    

    def edit_new_entity(self,username,new_entity_id,new_attribute):

        flag,newent= self.get_new_entity(username,new_entity_id)
        if flag == False:
            return False
        else:
            newent.entity_attributes = new_attribute

            newent.save_to_db()

            return True

    def review_new_entity(self,nwent_id,status):


        nwent = self.get_entity_by_id(nwent_id)

        nwent.status = status

        nwent.save_to_db()

        return True
        pass