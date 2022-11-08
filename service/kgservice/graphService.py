
from py2neo import Graph,Node,NodeMatcher,Relationship,Path



from app import graph
from utils.code import StatusCode

#todo 重构图谱的一个处理逻辑，这里先用老代码

class GraphService(object):
    def __init__(self):
        self.node_matcher = NodeMatcher(graph)
        


    def getNodeLabel(self,node):
        results = []
        labelset = node.labels
        results = list(labelset)

        return results


    '''
    def getNodeKey(node):
        results = list(node.keys())
        return results

    def getNodeValue(node):
        results = list(node.values())
        return results
    '''

    def genNodeDict(self,node):
        label = self.getNodeLabel(node)
        result = {}
        props = {}
        result['id'] = node.identity
        result['label'] = label
        props = dict(node)
        result['props'] = props
        result['name'] = props['name']
        return result
        

    def genLinkDict(self,path):
        label = list(path.types())[0]
        sid = path.start_node.identity
        tid = path.end_node.identity
        results = {}
        results['sid'] = sid
        results['tid'] = tid
        results['name'] = label

        return results

    def genRelDict(self,rel):
        label = type(rel).__name__
        sid = rel.start_node.identity
        tid = rel.end_node.identity
        results = {}
        results['sid'] = sid
        results['tid'] = tid
        results['name'] = label

        return results

    def appendNode(self,node,nodes):
        n = self.genNodeDict(node)
        if n not in nodes:
            nodes.append(n)

    def appendLink(self,link,links):
        l = self.genLinkDict(link)
        if l not in links:
            links.append(l)

    def appendRel(self,link,links):
        l = self.genRelDict(link)
        if l not in links:
            links.append(l)


    def get_init_graph(self):

        match_str = "MATCH p=(h)-[r]->(t) RETURN p,h,id(h),t,id(t),type(r),r LIMIT 50"
        resultslist = graph.run(match_str).data()

        Nodes,Links = self.decode_resultslist(resultslist)
        
        return StatusCode.OK,Nodes,Links

    def fuzzy_search(self,str):
        '''节点模糊搜索
        
        :str: 搜索关键字
        :return: Nodes
        '''

        match_str = 'match (m) where m.name contains \"'+ str +'\" return m' 
        resultslist = graph.run(match_str).data()

        Nodes,_ = self.decode_resultslist(resultslist)
        
        return StatusCode.OK,Nodes

    def get_one_hop_neighbor(self,id,limits="50"):
        '''获取节点一跳邻居
        
        :id: 节点id
        :limits: 限制结果数量
        :return: Nodes,Links
        '''

        match_str = ' MATCH p=(a)-[r]->(b) where id(a)='+ id + ' or id(b)='+id+' RETURN p LIMIT '+limits
        resultslist = graph.run(match_str).data()

        Nodes,Links = self.decode_resultslist(resultslist)

        return StatusCode.OK,Nodes,Links

    def get_two_hop_neighbor(self,id,limits="50"):
        '''获取节点两跳邻居
        
        :id: 节点id
        :limits: 限制结果数量
        :return: Nodes,Links
        '''

        
        match_str = ' MATCH p=(a)-[r]->(b)-[m]->(c) where id(a)='+ id + ' or id(c)='+ id +' RETURN p LIMIT ' + limits
        resultslist = graph.run(match_str).data()

        Nodes,Links = self.decode_resultslist(resultslist)

        return StatusCode.OK,Nodes,Links

    def decode_resultslist(self,resultslist):
        '''获取解析neo4j查询语句查询结果
        
        :resulutslist: 查询结果
        :return: Nodes,Links
        '''

        Nodes = []
        Links = []

        for r in resultslist:
            for t in list(dict(r).keys()):

                if  isinstance(r[t],Node):
                    self.appendNode(r[t],Nodes)
                
                elif  isinstance(r[t],Relationship):
             
                    self.appendNode(r[t].start_node,Nodes)
                    self.appendNode(r[t].end_node,Nodes)
                    self.appendRel(r[t],Links)
                  
                elif  isinstance(r[t],Path):
                    print(r[t].keys())
                    for n in r[t].nodes:
                        self.appendNode(n,Nodes)
                    for rel in r[t].relationships:
                        self.appendRel(rel,Links)

        return Nodes,Links
        