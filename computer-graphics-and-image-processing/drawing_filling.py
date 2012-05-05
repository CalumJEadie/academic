import debug
from drawing import *

class Polygon:

    def __init__(self,vertices):
        """
        Creates a polygon of >2 vertices.
        Assumes that polygon has no intersecting lines (not including vertices! :))
        """
    
        if len(vertices) < 3:
            raise ValueError
        self.vs = vertices
        
        
    def __str__(self):
        s = "Polygon("
        for v in self.vs[:-1]:
            s += "{0},".format(v)
        s += "{0})".format(v)
        return s
        
    def draw(self,wb,colour=None):
        
        for edge in self.edges():
            edge.draw(wb,colour)
        
    def edges(self):

        edges = []
        v_start = self.vs[0]
        for v_end in self.vs[1:]:
            edges.append(Line(v_start,v_end))
            v_start = v_end
        v_end = self.vs[0]
        edges.append(Line(v_start,v_end))
        return edges
        
def edge_compare_lowest_y(e0,e1):

    if e0.p0.y < e1.p0.y:
        return -1
    elif e0.p0.y > e1.p0.y:
        return 1
    else:
        return 0
        
def active_edge_compare_lowest_x(ae0,ae1):

    if ae0.edge.p0.x < ae1.edge.p0.x:
        return -1
    elif ae0.edge.p0.x > ae1.edge.p0.x:
        return 1
    else:
        return 0

def calculate_dx(line):
    return float(line.p1.x-line.p0.x)/float(line.p1.y-line.p0.y)
    
class ActiveEdge:

    def __init__(self,edge):
        """Encapsulates an active edge, it's dx and current x point of intersection.
        """
    
        self.edge = edge
        self.dx = calculate_dx(edge)
        self.x_intersection = edge.p0.x
        
    def __str__(self):
        return "ActiveEdge(edge:{0},dx:{1},x_intersection:{2})".format(self.edge,self.dx,self.x_intersection)

def fill(wb,polygon,colour=None):

    print "fill({0}".format(polygon)

    # Take all edges and put in an edge list, sorted on lowest y value.
    # Swap start and end points so start point has lowest y.
    # Remove horizontal edges.
    # Sort edges in ascending order of start point y.
    
    edges = polygon.edges()
    
    for i in range(0,len(edges)):
        if edges[i].p0.y > edges[i].p1.y:
            edges[i] = edges[i].reverse()
            
    edges = [edge for edge in edges if edge.p0.y != edge.p1.y]
            
    edges.sort(cmp=edge_compare_lowest_y)
    
    # Start with first scan line to intersect polygon.
    # Get all edges that intersect polygon and move them to active edge list.
    # For effeciency calculate the change in x for increment of y.
    
    scanline_y = edges[0].p0.y
    
    active_edges = [ActiveEdge(edges[0])]
    
    for edge in edges[1:]:
        if edge.p0.y == scanline_y:
            active_edges.append(ActiveEdge(edge))
        else:
            break # an optimisation as edges is sorted on y
            
    while len(active_edges) > 0:
            
        # For each edge in active edge list find the intersection points with the current
        # scanline. Sort into ascending order on x.
        
        active_edges.sort(cmp=active_edge_compare_lowest_x)
        
        # Fill between pairs of intersection points.
        
        for i in range(0,len(active_edges)-1,2):
            x0 = active_edges[i].x_intersection
            x1 = active_edges[i+1].x_intersection
            Line(Point(x0,scanline_y),Point(x1,scanline_y)).draw(wb,colour)
            
        # Move the next scanline.
        
        scanline_y += 1
        
        # Remove edges from active edge list if end point < scanline.
        
        active_edges = [active_edge for active_edge in active_edges if active_edge.edge.p1.y >= scanline_y]
        
        # Update intersection points.
        
        for edge in active_edges:
            edge.x_intersection += edge.dx
            
        # Add edges from edge list to active edge list if start point <= scanline and
        # was not previously in active edge list.
        
        active_edges.extend([ActiveEdge(edge) for edge in edges if edge.p0.y == scanline_y])
        
class Triangle(Polygon):

    def __init__(self,p0,p1,p2):
    
        Polygon.__init__(self,[p0,p1,p2])
        
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        
    def __str__(self):
        return "Triangle({0},{1},{2})".format(self.p0,self.p1,self.p2)
        
    @staticmethod
    def from_triangle(t):
    
        return Triangle(t.p0,t.p1,t.p2)
        
    def as_polygon(self):
        return Polygon(self.vs)
        
def evaluate_point_against_box_inequalities(box,point):
    return (point.x < box.xl, point.x > box.xr, point.y < box.yb, point.y > box.yt)
    
def subdivide_triangle_0_1(triangle):
    """
    Subdivides triangle by splitting along the line between the midpoint of points 0
    and 1 and point 2.
    """
    p = (triangle.p0+triangle.p1)/float(2)
    return (Triangle(triangle.p0,p,triangle.p2),Triangle(p,triangle.p1,triangle.p2))
    
def subdivide_triangle_1_2(triangle):

    p = (triangle.p1+triangle.p2)/float(2)
    return (Triangle(triangle.p0,triangle.p1,p),Triangle(triangle.p0,p,triangle.p2))
    
def subdivide_triangle_2_0(triangle):

    p = (triangle.p2+triangle.p0)/float(2)
    return (Triangle(triangle.p0,triangle.p1,p),Triangle(p,triangle.p1,triangle.p2))
        
def triangle_clipper(wb,box,triangle,division=0):

    if division > 3:
        return

    print "triangle_clipper({0},{1},{2})".format(box,triangle,division)
    
    triangle.draw(wb,colour="green")
    
    debug.pause()
    
    # Test whether triangle lies wholy inside, outside or staddles.
    p0 = triangle.p0
    p1 = triangle.p1
    p2 = triangle.p2
    
    (a0,b0,c0,d0) = evaluate_point_against_box_inequalities(box,p0)
    (a1,b1,c1,d1) = evaluate_point_against_box_inequalities(box,p1)
    (a2,b2,c2,d2) = evaluate_point_against_box_inequalities(box,p2)
    
    if a0 | b0 | c0 | d0 | a1 | b1 | c1 | d1 | a2 | b2 | c2 | d2 == False:
        # Wholy inside box.
        fill(wb,triangle.as_polygon(),colour="red")
    elif ((a0&a1&a2) | (b0&b1&b2) | (c0&c1&c2) | (d0&d1&d2)) == False:
        # There is no boundary for which all the points are on the side
        # that it outside of the box.
        # Need to clip.
        
        if a0:
            if a1 == False:
                (t1,t2) = subdivide_triangle_0_1(triangle)
            else:
                (t1,t2) = subdivide_triangle_2_0(triangle)
        elif a1 | a2:
            (t1,t2) = subdivide_triangle_1_2(triangle)
        elif b0:
            if b1 == False:
                (t1,t2) = subdivide_triangle_0_1(triangle)
            else:
                (t1,t2) = subdivide_triangle_2_0(triangle)
        elif b1 | b2:
            (t1,t2) = subdivide_triangle_1_2(triangle)
        elif c0:
            if c1 == False:
                (t1,t2) = subdivide_triangle_0_1(triangle)
            else:
                (t1,t2) = subdivide_triangle_2_0(triangle)
        elif c1 | c2:
            (t1,t2) = subdivide_triangle_1_2(triangle)
        elif d0:
            if d1 == False:
                (t1,t2) = subdivide_triangle_0_1(triangle)
            else:
                (t1,t2) = subdivide_triangle_2_0(triangle)
        elif d1 | d2:
            (t1,t2) = subdivide_triangle_1_2(triangle)
                
        triangle_clipper(wb,box,t1,division=division+1)
        triangle_clipper(wb,box,t2,division=division+1)
    
    # Wholy outside box.
    # Don't draw.
