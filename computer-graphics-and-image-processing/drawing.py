#! /usr/bin/python

"""
Implementing drawing algorithms from Computer Graphics and Image Processing.

http://www.cl.cam.ac.uk/teaching/1112/CompGraph/
"""

from Whiteboard import Point

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
