from py2neo import Node,NodeMatcher


from app import graph
from utils.code import StatusCode

class NodeService(object):
    def __init__(self):
        self.node_matcher = NodeMatcher(graph)


    def get_node_by_name(self,name):
        '''通过名字获取图谱实体
        
        :name: 名字
        :return: Node
        '''

        node = self.node_matcher.match(name=name).first()

        print(node)

        if node is None:
            return StatusCode.NODE_NOTEXIST,None 
        else:
            return StatusCode.OK, node
    
