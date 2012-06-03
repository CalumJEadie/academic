from graph import *
from disjoint_set import *
from priority_queue import *

def breadth_first_search(g,value):
    """
    Searchs for node with value "value" in graph "g".
    
    Uses specialisation of graph seach algorithm from Artifical Intelligence I.
    """
    
    closed = [] # All expanded nodes
    fringe = [g.vs[0]] # Nodes found and to be explored
    
    while True:
        
        if len(fringe) == 0:
            return False
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
            return False
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
            topological_sort_visit(g,v)
    u.color = Color.BLACK
    time += 1
    u.finished = time
    linear_ordering.append(u)
    return time
    
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
    
    vertex_forest = DisjointSetCollection()
    spanning_tree_edges = []
    for v in g.vs:
        vertex_forest.make_set(v)
    for e in sorted(g.es,cmp=lambda x,y: cmp(x,y), key=lamba x:x.w):
        if vertex_forest.find_set(e.s) != vertex_forest.find_set(e.d):
            spanning_tree_edges.append(e)
            vertex_forest.union(e.s,e.d)
    return spanning_tree_edges
    
def prim(g):
    """
    Prim's algorithm for finding a minimum spanning tree.
    
    1. Select any node to be the first node.
    2. Consider arcs which connect to nodes in T to nodes outside T,
       pick one with least weight.
    3. Repeat (2) until all nodes choosen.
    """
    
    # This is not a working implementation as the interface of PriorityQueue
    # does not allow specification of keys in constructor.
    
    for u in g.vs:
        u.key = PriorityQueue.INFINITY
        u.prev = None
    root = g.vs[0]
    root.key = 0
    v_queue = PriorityQueue(g.vs)
    while len(v_queue) > 0:
        u = v_queue.extract_min()
        for v in g.adjacent(u)
            e = g.edge(u,v)
            if v in v_queue and e.w < v.key
                v.prev = u
                v.key = e.w

def initialize_single_source(g,source):
    """
    From Introduction to Algorithms pg 648.
    """
    
    for v in g.vs:
        v.d = Graph.INFINITY
        v.prev = None
    source.d = 0
    
def relax(g,u,v):
    """
    Test whether can improve the shortest path to v found so far by going
    through u and if so updating shortest path estimate v.d and predecessor
    v.prev.
    
    From Introduction to Algorithms pg 649.
    """
    
    assert u in g.vs
    assert v in g.vs
    
    e = g.edge(u,v)
    if v.d > ( u.d + e.w ):
        v.d = u.d + e.w
        v.prev = u

def bellman_ford(g,source):
    """
    Implementation of Bellman-Ford algorith for finding shortest path
    to all vertices from source vertex "source".
    
    Solves the single source shortest paths problem in the general case
    where edge weights may be negative. Checks whether there is a negative
    weight cycle that is reachable from the source, if there is such a cycle
    then no solution exists, if there is not such a cycle then algorithms produces
    the shortest paths and their weights.
    
    From Introduction to Algorithms pg 651.
    """
    
    assert source in g.vs
    
    initialize_single_source(g,source)
    for i in range(0,len(g.vs)): # len(g.vs)-1 times
        for e in g.es:
            relax(g,e.s,e.d)
    for e in g.es:
        (u,v) = (g.es.s,g.es.d)
        if v.d > u.d + e.w:
            return False
    return True
    
def dijksta(g,source):
    """
    Implementation of Dijkstra's algorithm for finding shortest path
    to all vertices from source vertex "source".
    
    Solves the single source shortest paths problem for the case where
    all edge weights are non negative.
    
    From Introduction to Algorithms pg 658.
    """
    
    initialize_single_source(g,source)
    v_shortest_path_determined = set()
    v_not_explored = PriorityQueue(g.vs)
    while len(v_not_explored) > 0:
        u = v_not_explored.extract_min()
        v_shortest_path_determined.add(u)
        for v in g.adjacent(u)
            relax(g,u,v)
            
def ford_fulkerson(g):
    for e in g.es:
        e.flow = 0
    augmenting_paths = []
    while True:
        augmenting_path = find_augementing_path(g,augmenting_paths)
        if augmenting_path != False:
            augumenting_paths.append(augmenting_path)
        else:
            return augmenting_paths
            
def bipartite_matching(l,r,es):
    """
    Solve bipartite matching problem by transforming to maximum flow.
    
    ls,rs - vertices
    es - edges between partitions
    """
    
    g = Graph(ls+rs,es)
    
    # Add unit capacities to edges from left to right partition
    for e in es:
        e.capacity = 1
    
    # Add supersource and supersink
    super_source = V()
    super_sink = V()
    g.vs + [super_source,super_sink]
    for l in ls:
        g.es.append(E(super_source,l,1)
    for r in rs:
        g.es.append(E(r,super_sink,1)
    
    max_flow = find_maximum_flow(g,super_source,super_sink)
    
    return max_flow
