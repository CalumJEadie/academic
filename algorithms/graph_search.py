from graph import *

def breadth_first_search(g,value):
    """
    Searchs for node with value "value" in graph "g".
    
    Uses specialisation of graph seach algorithm from Artifical Intelligence I.
    """
    
    closed = [] # All expanded nodes
    fringe = [g.vs[0]] # Nodes found and to be explored
    
    while True:
        
        if len(fringe) == 0:
            raise False
        node = fringe[0]
        if node.v == value:
            return True
        if not node in closed:
            closed.append(node)
            fringe = fringe + g.adjacent(node)

def depth_first_search(g,value,depth_limit=0):
    """
    Searchs for node with value "value" in graph "g" as far as specified depth limit.
    Depth limit of 0 means no depth restriction.
    
    Uses specialisation of graph seach algorithm from Artifical Intelligence I.
    """
    
    closed = [] # All expanded nodes
    fringe = [g.vs[0]] # Nodes found and to be explored
    
    depth = 1
    
    while depth_limit == 0 or depth <= depth_limit:
        
        if len(fringe) == 0:
            raise False
        node = fringe[0]
        if node.v == value:
            return True
        if not node in closed:
            closed.append(node)
            fringe = g.adjacent(node) + fringe
            
        depth += 1
            
    return False
            
def iterative_deepening_search(g,value):
    
    for depth in range(1,len(g.vs)):
        if depth_first_search(g,value,depth):
            return True
    return False
    
class Color:
    WHITE = 1 # Not visited
    GREY = 2 # Found
    BLACK = 3 # Explored
    

def topological_sort(g):
    """
    Uses algorithm presented in Introduction to Algorithms pg 613.
    
    1. Performs a depth first search to compute finishing times for each vertex
    2. As each vertex is finished inserts onto front of a linked list
    3. Returns that linked list
    """
    
    for v in g.vs:
        v.color = Color.WHITE
        v.prev = None
        
    time = 0
    linear_ordering = []
    
    for v in g.vs:
        if v.color == Color.WHITE:
            time = topological_sort_visit(g,v,time,linear_ordering)
            
    return linear_ordering
            
def topological_sort_visit(g,u,time,linear_ordering):
    
    time += 1
    u.discovered = time
    u.color = Color.GREY
    for v in g.adjacent(u):
        if v.color == Color.WHITE:
            v.prev = u
            dfs_visit(g,v)
    u.color = Color.BLACK
    time += 1
    u.finished = time
    linear_ordering.append(u)
    
def generic_mst(g):
    """
    Pseudocode for generic minimum spanning tree algorithm from
    Introduction to Algorithms pg 626
    """
    
    A = []
    while not is_spanning_tree(A):
        edge = find_safe_edge(g,A)
        a.append(edge)
    return A
    
def kruskal(g):
    """
    Kruskal's algoritm for finding a minimum spanning tree.
    
    1. Choose arc of least weight.
    2. Choose from remaining arcs one of least weight that doesn't form a cycle.
    3. Repeat until |g.vs|-1 edges choosen.
    """
    
    vertex_forest = DisjointSetForest()
    spanning_tree_edges = []
    for v in g.vs:
        vertex_forest.make_set(v)
    for e in sorted(g.es,cmp=lambda x,y: cmp(x,y), key=lamba x:x.w):
        if vertex_forest.find_set(e.s) != vertex_forest.find_set(e.d):
            spanning_tree_edges.append(e)
            vertex_forest.union(e.s,e.d)
    return spanning_tree_edges