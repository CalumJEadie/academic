"""
A collection of simple data structures for representing graphs.
"""

class Graph():
    """
    A representation of a graph using an adjacency list.
    """
    
    INFINITY = float('inf')
    
    vs = []
    es = []
    
    def __init__(self,vs,es):
        self.vs = vs
        self.es = es
        
    def adjacent(self,vertex):
        adjacent = []
        for e in self.es:
            if e.s == vertex:
                adjacent.append(e.d)
            elif e.d == vertex:
                adjacent.append(e.s)
        return adjacent
        
    def edge(self,u,v):
        for e in es:
            if e.s == u and e.d == v:
                return e
        return False
        
class V():
    """
    A vertex.
    """
    
    v = None # Value
    l = "" # Label
    
    def __init__(self,v=None,l=""):
        self.v = v
        self.l = l
        
    def __repr__(self):
        return "V(%s,%s)" % (self.v,self.l)
    
class E():
    """
    An edge.
    """
    
    s = None # Source
    d = None # Destination
    w = None # Weight
    
    def __init__(self,s,d,w=None):
        self.s = s
        self.d = d
        self.w = w
        
    def __repr__(self):
        return "E(%s,%s,%s)" % (self.s,self.d,self.w)
        
class Tree(V):
    """
    A representation of a n-ary tree.
    """
    
    def __init__(self,v=None,children=[],l=""):
        V.__init__(self,v,l)
        self.children = children
        
    def to_graph():
        """
        Converts into graph representation of the graph underlying the tree.
        
        Performs a depth first search.
        """
        
        if len(self.children) == 0:
            
            return Graph([self],[])
            
        else:
            
            es = []
            vs = [self]
            for child in self.children:
                child_graph = child.to_graph()
                vs.extend(child_graph.vs)
                es.extend(child_graph.es)
                es.append(E(self,child))
                
            return Graph(vs,es)
            
    def __str__(self):
        
        def indent(s):
            return '\n'.join(map(lambda x: (" "*4)+x,s.splitlines()))
        
        if len(self.children) == 0:
            
            return "Tree(%s,%s)" % (self.l,self.v)
            
        else:
            
            s = "Tree(%s,%s,[\n" % (self.l,self.v)
            s += '\n'.join(map(lambda x: indent(str(x)),self.children))
            s += "\n)"
            return s