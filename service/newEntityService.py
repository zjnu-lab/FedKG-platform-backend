from models.new_entity import NewEntity
from service import user_service

class NewEntityService(object):
    
    def __init__(self):
        pass

    def create_new_entity(self, username,args):
        is_success = False
        

        user = user_service.get_user(username)

        new_entity = NewEntity(user_id = user.id)

        # 序列化 args
        #todo
        new_entity.entity_attributes = args
        
        
        new_entity.save_to_db()
        is_success = True
        
        return is_success

    def get_user_new_entities(username):
        user = user_service.get_user(username)

        user_new_entities = user.new_entities

        return user_new_entities



    def get_all_new_entities():
        pass

    def delete_new_entity(new_entity_id):
        pass

    def review_new_entity(new_entity_id,status):
        pass