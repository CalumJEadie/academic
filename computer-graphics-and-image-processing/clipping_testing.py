#! /usr/bin/python

from Whiteboard import Point
from WhiteboardWindow import *
import threading
import drawing
import debug

class ClippingTest(WhiteboardWindow,threading.Thread):

    def __init__(self):

        WhiteboardWindow.__init__(self,defaultPeriod=0,height=100,width=100)        
        threading.Thread.__init__(self)
        self.daemon = True
        
    """Perform testing in different thread to allow for viewing progress of algorithms
    in real time."""
    def run(self):
    
        box = drawing.BoundingBox(25,75,35,55)
        
        lines = [
            drawing.Line(drawing.Point(30,30),drawing.Point(60,60)),
            drawing.Line(drawing.Point(10,30),drawing.Point(60,30)),
            drawing.Line(drawing.Point(10,50),drawing.Point(80,40))
        ]
        
        for line in lines:
            drawing.cohan_sutherland_clipper(self,box,line)
#            debug.pause()

        p0 = Point(50,50)
        p1s = drawing.square(p0,60,5)
        
        for p1 in p1s:
            drawing.cohan_sutherland_clipper(self,box,drawing.Line(p0,p1))

l = ClippingTest()
l.start()
l.mainloop()
