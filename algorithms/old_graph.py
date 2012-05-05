class Node(list):
    """A node. May have a label."""

    label = None
    edges = []
    
    def __init__(self,edges=[],label=None):
    
        super(Node,self).__init__(edges)
        self.label = label
        
    def __repr__(self):
    
        return "Node(%s,%s)" % (self.edges,self.label)
        
    def __str__(self):
    
        return "Node(#edges:%s,label:%s)" % (len(self.edges),self.label)
        
    def append(self,node,value=None):
        
        super(Node,self).append(Edge(self,node,value))
        
    @staticmethod
    def from_subtree(children):
    
        root = Node()
    
        for child in children:
            root.append(child)
            
        return root
    
class Edge():
    """An edge between nodes. May have a value."""    

    value = None
    source = None
    dest = None
    
    def __init__(self,source,dest,value=None):
    
        self.source = source
        self.dest = dest
        self.value = value
        
    def __str__(self):
    
        source = self.source.label if self.source.label is not None else hex(id(self.source))
        dest = self.dest.label if self.dest.label is not None else hex(id(self.dest))
    
        if self.value is None:
            return "%s --> %s" % (source,dest)
        else:
            return "%s -(%s)-> %s" % (source,self.value,dest)
