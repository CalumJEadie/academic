#! /usr/bin/python

"""
Implementing drawing algorithms from Computer Graphics and Image Processing.

http://www.cl.cam.ac.uk/teaching/1112/CompGraph/
"""

from Whiteboard import Point
import math

# To not distract from algorithms will use wb for WhiteboardWindow.

def bresenham1(wb,p1,p2):

    print "Bresenham #1: {0} -> {1}".format(p1,p2)
    
    d = float(p2.y-p1.y)/(p2.x-p1.x)
    x = p1.x
    yi = p1.y
    y = p1.y
    wb.draw(Point(x,y))
    
    while x < p2.x:
        x += 1
        yi += d
        y = round(yi)
        wb.draw(Point(x,y))
        
def bresenham2(wb,p1,p2):

    if p1.x == p2.x:
        # Line are vertical
        x = p1.x
        for y in range(p1.y,p2.y+1):
            wb.draw(Point(x,y))
    else:
        # Line are not vertical
        dx = p2.x-p1.x
        dy = p2.y-p1.y
        dydx = float(dy)/dx
        
        # Determine which per quadrant method to use.
        if dy > 0:
            if dx > 0:
                if dydx <= 0.5:
                    bresenham2_1(wb,p1,p2)
                else:
                    bresenham2_2(wb,p1,p2)
            else:
                if dydx <= -0.5:
                    bresenham2_3(wb,p1,p2)
                else:
                    bresenham2_4(wb,p1,p2)
        else:
            if dx > 0:
                if dydx <= -0.5:
                    bresenham2_3(wb,p2,p1)
                else:
                    bresenham2_4(wb,p2,p1)
            else:
                if dydx <= 0.5:
                    bresenham2_1(wb,p2,p1)
                else:
                    bresenham2_2(wb,p2,p1)
                    
def bresenham2_1(wb,p1,p2):

    print "Bresenham #2_1: {0} -> {1}".format(p1,p2)
    
    dydx = float(p2.y-p1.y)/(p2.x-p1.x)
    x = p1.x
    yi = p1.y
    y = p1.y
    wb.draw(Point(x,y))
    
    while x < p2.x:
        x += 1
        yi += dydx
        y = round(yi)
        wb.draw(Point(x,y))
                    
def bresenham2_2(wb,p1,p2):

    print "Bresenham #2_2: {0} -> {1}".format(p1,p2)
    
    dxdy = float(p2.x-p1.x)/(p2.y-p1.y)
    x = p1.x
    xi = p1.x
    y = p1.y
    wb.draw(Point(x,y))
    
    while y < p2.y:
        xi += dxdy
        y += 1
        x = round(xi)
        wb.draw(Point(x,y))
                    
def bresenham2_3(wb,p1,p2):

    print "Bresenham #2_3: {0} -> {1}".format(p1,p2)
    
    dxdy = float(p2.x-p1.x)/(p2.y-p1.y)
    x = p1.x
    xi = p1.x
    y = p1.y
    wb.draw(Point(x,y))
    
    while y < p2.y:
        xi += dxdy
        y += 1
        x = round(xi)
        wb.draw(Point(x,y))
                    
def bresenham2_4(wb,p1,p2):

    print "Bresenham #2_4: {0} -> {1}".format(p1,p2)
    
    dydx = float(p2.y-p1.y)/(p2.x-p1.x)
    x = p1.x
    yi = p1.y
    y = p1.y
    wb.draw(Point(x,y))
    
    while x > p2.x:
        x -= 1
        yi -= dydx
        y = round(yi)
        wb.draw(Point(x,y))
        
def midpoint_line(wb,p1,p2):

    print "Midpoint Line: {0} -> {1}".format(p1,p2)
    
    a = p2.y-p1.y
    b = -(p2.x-p1.x)
    c = p2.x*p1.y - p1.x*p2.y
    x = round(p1.x)
    y = round(p1.y - ((x-p1.x)/(float(a)/b)))
    d = a*(x+1) + b*(y+0.5) + c
    
    wb.draw(Point(x,y))
    
    while x < (p2.x-0.5):
        x += 1
        if d < 0:
            d += a
        else:
            d += a + b
            y += 1
        wb.draw(Point(x,y))
        
"""Uses midpoint circle algorithm to draw circle of integer radius r centered at
the o."""
def midpoint_circle(wb,o,r):

    print "Midpoint Circle (Origin): Radius {0}".format(r)
    
    # Consider 2nd octant and use symmetry for the rest.
    x0 = 0
    y0 = r
    sqrt2 = 1.41
    x1 = round(r / sqrt2) # Using pi/4 special trangle
    
    x = x0
    y = y0
    
    midpoint_circle_draw(wb,o,Point(x,y))
    
    # Decision variable d = x^2 + y^2 - r^2
    
    d = x**2 + y**2 - r**2
    
    while x < (x1-0.5):
        x += 1
        if d < 0:
            # Go east.
            d += 2*x + 1 # d' = (x+1)^2 + y^2 - r^2 = d + 2x + 1
        else:
            # Go south east.
            d += 2*x -2*y + 2 # d' = (x+1)^2 + (y+1)^2 - r^2 = d + 2x -2y + 2
            y -= 1
        midpoint_circle_draw(wb,o,Point(x,y))

"""Takes a point to be drawn in the 2nd quadrant of circle with origin o at offset p
and draws points in all quadrants.
"""
def midpoint_circle_draw(wb,o,p):
    wb.draw(Point(o.x+p.y,o.y+p.x)) # Quadrant 1
    wb.draw(Point(o.x+p.x,o.y+p.y)) # Quadrant 2
    wb.draw(Point(o.x-p.x,o.y+p.y)) # Quadrant 3
    wb.draw(Point(o.x-p.y,o.y+p.x)) # Quadrant 4
    wb.draw(Point(o.x-p.y,o.y-p.x)) # Quadrant 5
    wb.draw(Point(o.x-p.x,o.y-p.y)) # Quadrant 6
    wb.draw(Point(o.x+p.x,o.y-p.y)) # Quadrant 7
    wb.draw(Point(o.x+p.y,o.y-p.x)) # Quadrant 8
    
class Line:

    def __init__(self,p0,p1):
    
        self.p0 = p0
        self.p1 = p1
        
    def interpolate(self,s):
    
        return Point((1-s)*self.p0.x+s*self.p1.x,(1-s)*self.p0.y+s*self.p1.y)
        
    def draw(self,wb):
    
        bresenham2(wb,self.p0,self.p1)
    
class BezierCubic:

    def __init__(self,p0,p1,p2,p3):
    
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
def bezier_cubic(wb,curve,tolerance):

    if is_bezier_cubic_flat(curve,tolerance):
    
        bresenham2(wb,curve.p0,curve.p3)
        
    else:
    
        (left,right) = subdivide_bezier_cubic(curve)
        bezier_cubic(wb,left,tolerance)
        bezier_cubic(wb,right,tolerance)
    
def subdivide_bezier_cubic(curve):

    q0 = curve.p0
    q1 = 0.5*curve.p0 + 0.5*curve.p1
    q2 = 0.25*curve.p0 + 0.5*curve.p1 + 0.25*curve.p2
    q3 = 0.125*curve.p0 + 0.375*curve.p1 + 0.375*curve.p2 + 0.125*curve.p3
    
    r0 = 0.125*curve.p0 + 0.375*curve.p1 + 0.375*curve.p2 + 0.125*curve.p3
    r1 = 0.25*curve.p1 + 0.5*curve.p2 + 0.25*curve.p3
    r2 = 0.5*curve.p2 + 0.5*curve.p3
    r3 = curve.p3
    
    left = BezierCubic(q0,q1,q2,q3)
    right = BezierCubic(r0,r1,r2,r3)
    
    return (left,right)

"""Test whether curve lies within tolerance of line between curve.p0 and curve.p3
by checking position of control points curve.p1 and curve.p2.
"""
def is_bezier_cubic_flat(curve,tolerance):

    return dist_point_to_line(Line(curve.p0,curve.p3),curve.p1) < tolerance and dist_point_to_line(Line(curve.p0,curve.p3),curve.p2) < tolerance
    
def dist_point_to_point(p0,p1):

    return ((p1.x-p0.x)**2+(p1.y-p1.x)**2)**0.5
    
def dist_point_to_line(line,p):

    l0 = line.p0
    l1 = line.p1

    sn = ((l1.x-l0.x)*(p.x-l0.x) + (l1.y-l0.y)*(p.y-l0.y))
    sd = ((l1.x-l0.x)**2 + (l1.y-l0.y)**2)
    if sd == 0:
        sd = 0.0000000001
    s = sn/sd
    
    if s<0:
        # Beyond end of line, nearest to l0.
        return dist_point_to_point(l0,p)
    elif s>1:
        # Beyond end of line, nearest to l1.
        return dist_point_to_point(l1,p)
    else:
        return dist_point_to_point(line.interpolate(s),p)
        
class BoundingBox:

    def __init__(self,xl,xr,yb,yt):
        self.xl = xl
        self.xr = xr
        self.yb = yb
        self.yt = yt
        
def cohan_sutherland_clipper(box,line):

    l0 = line.p0
    l1 = line.p1

    # 4 bit code, one bit for each inquality
    a0 = l0.x < box.xl
    b0 = l0.x > box.xr
    c0 = l0.y < box.yl
    d0 = l0.y > box.yr
    
    a1 = l1.x < box.xl
    b1 = l1.x > box.xr
    c1 = l1.y < box.yl
    d1 = l1.y > box.yr
    
    if (a0 | b0 | c0 | d0 | a1 | b1 | c1 | d1) == False:
        # Accept
        line.draw()
    elif ((a0&a1) | (b0&b1) | (c0&c1) | (d0&d1)) == False:
        # Need to clip
        
        return NotImplemented
        
    # Otherwise reject, both ends outside.
