#! /usr/bin/python

from Whiteboard import Point
from WhiteboardWindow import *
import threading
import drawing

class CurveTest(WhiteboardWindow,threading.Thread):

    def __init__(self):

        WhiteboardWindow.__init__(self,defaultPeriod=0)        
        threading.Thread.__init__(self)
        self.daemon = True
        
    """Perform testing in different thread to allow for viewing progress of algorithms
    in real time."""
    def run(self):

        curves = []
        
        curves.append(drawing.BezierCubic(Point(10,10),Point(10,40),Point(90,60),Point(90,20)))

        for curve in curves:
            drawing.bezier_cubic(self,curve,5)

l = CurveTest()
l.start()
l.mainloop()
