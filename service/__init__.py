from imp import new_module
from service.userService import UserService


user_service = UserService()

from service.newEntityService import NewEntityService
new_entity_service = NewEntityService()


from service.kgservice.nodeService import NodeService

node_service = NodeService()

from service.kgservice.graphService import GraphService

graph_service = GraphService()

from service.taskService import TaskService

task_service = TaskService()

from service.modelService import ModelService

model_service = ModelService()