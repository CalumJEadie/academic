#! /usr/bin/python

from Whiteboard import Point
from WhiteboardWindow import *
import threading
import drawing
import debug

class CurveTest(WhiteboardWindow,threading.Thread):

    def __init__(self):

        WhiteboardWindow.__init__(self,defaultPeriod=0)        
        threading.Thread.__init__(self)
        self.daemon = True
        
    """Perform testing in different thread to allow for viewing progress of algorithms
    in real time."""
    def run(self):
    
        assert drawing.dist_point_to_point(Point(0,0),Point(10,0)) == 10
        assert drawing.dist_point_to_point(Point(0,0),Point(3,4)) == 5

        curves = []

        curves.append(drawing.BezierCubic(Point(10,10),Point(10,10),Point(90,10),Point(90,10)))
        curves.append(drawing.BezierCubic(Point(10,10),Point(10,10),Point(90,20),Point(90,20)))        
        curves.append(drawing.BezierCubic(Point(10,10),Point(10,40),Point(90,60),Point(90,20)))

        for curve in curves:
            drawing.bezier_cubic(self,curve,5)

        debug.pause()
        self.clear()
            
        for curve in curves:
            drawing.bezier_cubic(self,curve,2)
            
        debug.pause()
        self.clear()
            
        for curve in curves:
            drawing.bezier_cubic(self,curve,1)

l = CurveTest()
l.start()
l.mainloop()
