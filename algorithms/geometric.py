CLOCKWISE = 0;
ANTICLOCKWISE = 1;
SAME = 2;

class Vector():
    
    x = None
    y = None
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)

class Line():
    
    start = None
    end = None
    
    def __init__(self,start,end):
        self.start = start
        self.end = end
        
def cross(p,q):
    """
    Calculate the direction of the z component of the cross product of the 
    three dimensional vectors [p.x,p.y,0] and [q.x,q.y,0].
    """
    
    return p.x*q.y - p.y*q.x
        
def direction(o,p,q):
    """
    Calculate the relative direction of line segments o->p and o->q.
    
    CLOCKWISE means q is clockwise from p.
    """
    
    return {
        -1: CLOCKWISE
        0: SAME
        1: ANTICLOCKWISE
    }[cross(p-o,q-o)]
    
def intersect(a,b):
    """
    Determine whether or not two lines a and b intersect.
    
    DOES NOT HANDLE BOUNDARY CASES WHERE ONE END ON SEGMENT.
    """
    
    direction_b_start_from_a = direction(a.start,a.end,b.start)
    direction_b_end_from_a = direction(a.start,a.end,b.end)
    
    if direction_b_start_from_a == direction_b_end_from_a:
        return False
    else:
        # Start and end points of line b are on different sides of line a.
        direction_a_start_from_b = direction(b.start,b.end,a.start)
        direction_a_end_from_b = direction(b.start,b.end,a.end)
        
        if direction_a_start_from_b == direction_a_end_from_b:
            return False
        else:
            return True
            
def graham_scan(ps):
    """
    Finds convex hull of a set of points.
    
    Maintain a stack of candidate points. Pushes each point of inpurt set ps
    onto the stack on at a time. Pops from the stack each point that is not
    a vertex of the convex hull.
    """
    
    def cmp_y_coord_then_x_coord(a,b):
        return cmp((a.y,a.x),(b.y,b.x)
        
    ps.sort(cmp=cmp_y_coord_then_x_coord)
    
    lowest_point = ps.pop(0)
    
    def cmp_polar_angle_relative_to_lowest_point(p,q):
        """
        HANDLING POINTS WITH SAME POLAR ANGLE OMITTED.
        WOULD NEED TO REMOVE ALL BUT FURTHEST.
        """
        return cross(p-lower_point,q-lowest_point)
        
    def non_left_turn(p,q,r):
        return direction(p,q,r) == CLOCKWISE
        
    ps.sort(cmp=cmp_polar_angle_relative_to_lowest_point)
    
    p_stack = []
    
    p_stack.append(lowest_point)
    p_stack.append(p[0])
    p_stack.append(p[1])
    for i in range(2,len(p)):
        while non_left_turn(p_stack[-2],p_stack[-1],p[i]):
            s.pop()
        s.append(p[i])