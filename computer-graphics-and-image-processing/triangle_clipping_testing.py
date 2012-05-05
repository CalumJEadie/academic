#! /usr/bin/python

from Whiteboard import Point
from WhiteboardWindow import *
import threading
import drawing
import drawing_filling
import debug

class ClippingTest(WhiteboardWindow,threading.Thread):

    def __init__(self):

        WhiteboardWindow.__init__(self,defaultPeriod=0,height=100,width=100)        
        threading.Thread.__init__(self)
        self.daemon = True
        
    """Perform testing in different thread to allow for viewing progress of algorithms
    in real time."""
    def run(self):
    
        box = drawing.BoundingBox(25,75,30,70)
        triangles = [
            drawing_filling.Triangle(Point(10,10),Point(90,10),Point(50,90))
        ]
        
        for triangle in triangles:
            triangle.draw(self)
            drawing_filling.triangle_clipper(self,box,triangle)

l = ClippingTest()
l.start()
l.mainloop()
