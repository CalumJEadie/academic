"""
A collection of simple data structures for representing graphs.
"""

class Graph():
    """
    A representation of a graph using an adjacency list.
    """
    
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