from imp import new_module
from service.userService import UserService


user_service = UserService()

from service.newEntityService import NewEntityService
new_entity_service = NewEntityService()
