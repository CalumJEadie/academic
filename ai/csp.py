"""
Constraint Satisfaction Problems

Set of n variables V1,V2,...,Vn
For each Vi a domain Di
A set of m constraints C1,C2,...,Cm

Each constraint specifies an allowable collection of values for a set of variables

Eg. Graph colouring

Vi = node i
Di = {B,R,C}

C1 = (
    (V1,V2),
    [(B,R),(B,C),...]
)
"""

class Problem():
    
    num_variables = 0
    domains = []
    constraints = [] # Constraints implemented as an array of associative arrays.
    
    def __init__(self,num_variables,domains,constraints):
        assert(num_variables == len(domains)
        self.num_variables = num_variables
        for c in constraints:
            for k,v in c:
                assert k > 0 && k < num_variables # Constraint refers to a variable in a problem
                assert v in domains[i] # Constraint refers to a value in the variables domain
        self.constraints = constraints

def backtracking_search(g):
    
    def get_next_var(assignments):
        pass
        
    def order_vars(next_var,assignments):
        pass
        
    def consistent(var,assignment):
        pass
    
    def search(assignments):
        
        if complete(assignments):
            return assignments
            
        next_var = get_next_var(assignments):
        
        for v in order_vars(next_var,assignments):
            if consistent(v,assignments):
                assignments.append((next_var,v))
                solution = bt(assignments)
                if solution is not False:
                    return solution
                assignments.remove((next_var,v))
                
        return False
        
    return search([])