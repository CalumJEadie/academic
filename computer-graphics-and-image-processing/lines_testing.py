#! /usr/bin/python

from Whiteboard import Point
from WhiteboardWindow import *
import threading
import drawing

class LineTest(WhiteboardWindow,threading.Thread):

    def __init__(self):

        WhiteboardWindow.__init__(self,defaultPeriod=0,height=200,width=200)        
        threading.Thread.__init__(self)
        self.daemon = True
        
    """Perform testing in different thread to allow for viewing progress of algorithms
    in real time."""
    def run(self):
    
        p0 = Point(50,50)
        p1s = drawing.square(p0,70,5)
        for p1 in p1s:
            self.draw(p1)
    
#        for x in range(10,14):
#            for y in range(10,14):
#                self.draw(Point(x,y))
#                
#        for i in range(0,10):
#            drawing.bresenham1(self,Point(30,30),Point(40,30+(5*i)))
#                
#        for i in range(0,10):
#            drawing.bresenham2(self,Point(60,30),Point(90,30+(7*i)))
            
#        origin = Point(50,50)
#        x = 70
#        y = 30
#        step = 5
#        while y < 70:
#            drawing.bresenham2(self,origin,Point(x,y))
#            y += step
#        while x > 30:
#            drawing.bresenham2(self,origin,Point(x,y))
#            x -= step
#        while y > 30:
#            drawing.bresenham2(self,origin,Point(x,y))
#            y -= step
#        while x < 70:
#            drawing.bresenham2(self,origin,Point(x,y))
#            x += step

        p0 = Point(50,50)
        p1s = drawing.square(p0,40,5)
        for p1 in p1s:
#            drawing.midpoint_line(self,p0,p1)
            self.draw(p1)
            drawing.bresenham2(self,p0,p1)

        p0 = Point(100,100)
        p1s = drawing.square(p0,60.5,5)
        for p1 in p1s:
#            drawing.midpoint_line(self,p0,p1)
            self.draw(p1)
            drawing.bresenham2(self,p0,p1)
            
        drawing.bresenham2(self,Point(10,10),Point(80,10),colour="red")

l = LineTest()
l.start()
l.mainloop()
