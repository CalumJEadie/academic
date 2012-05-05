from algorithms.graph import *

def start_rbfs(g,goaltest,start_state):
    return rbfs(g,goaltest,u,Graph.INFINITY)

def rbfs(g,goaltest,u,f_limit):
    """
    Implementation of Recursive Best Fit Search from Aritifical Intelligence I
    course notes slide 106.
    """
    
    get_f = lambda x: return x.f
    
    if goaltest(n):
        return n
        
    vs = list(g.adjacent(u)) # vs = Successors of u
    
    if len(vs): # u has no successors
        return (False,Graph.INFINITY)
        
    for v in vs:
        v.f = max(v.f,u.f) # Ensures monotonicity of f
        
    while True:
        vs.sort(None,get_f) # Sort on f
        best_v = vs[0]
        if best_v.f > f_limit:
            return (False,best_v.f)
        next_best_v = vs[1]
        (goal,f) = rbfs(best,min(g,goaltest,f_limit,next_best_v)
        best_v.f = f
        if goal != False:
            return goal