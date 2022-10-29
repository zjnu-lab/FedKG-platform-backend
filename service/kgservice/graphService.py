
from py2neo import Node,NodeMatcher


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

        Nodes = []
        Links = []

        for r in resultslist:
            hnode = self.genNodeDict(r['h'])
            tnode = self.genNodeDict(r['t'])
            if hnode not in Nodes:
                #hnode['id'] = len(Nodes)+1
                Nodes.append(hnode)
            if tnode not in Nodes:
                #tnode['id'] = len(Nodes)+1
                Nodes.append(tnode)

            link = self.genLinkDict(r['p'])
            Links.append(link)
        
        return StatusCode.OK,Nodes,Links

    def fuzzy_search(self,str):

        match_str = 'match (m) where m.name contains \"'+ str +'\" return m' 
        resultslist = graph.run(match_str).data()


        Nodes = []
        
        for r in resultslist:
            # node = self.genNodeDict(r['m'])
            Nodes.append(dict(r['m']))

        return StatusCode.OK,Nodes