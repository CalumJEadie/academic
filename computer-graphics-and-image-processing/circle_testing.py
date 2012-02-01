#! /usr/bin/python

from Whiteboard import Point
from WhiteboardWindow import *
import threading
import drawing

class CircleTest(WhiteboardWindow,threading.Thread):

    def __init__(self):

        WhiteboardWindow.__init__(self,defaultPeriod=0)        
        threading.Thread.__init__(self)
        self.daemon = True
        
    """Perform testing in different thread to allow for viewing progress of algorithms
    in real time."""
    def run(self):
    
        drawing.midpoint_circle(self,Point(50,50),20)
        drawing.midpoint_circle(self,Point(50,50),30)
        drawing.midpoint_circle(self,Point(50,50),35)
        drawing.midpoint_circle(self,Point(50,50),40)

l = CircleTest()
l.start()
l.mainloop()
