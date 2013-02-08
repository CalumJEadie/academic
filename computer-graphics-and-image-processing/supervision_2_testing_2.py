#! /usr/bin/env python

"""
Computer Graphics and Image Processing - Supervision #2
Calum J. Eadie
"""

from Whiteboard import Point
from WhiteboardWindow import *
import threading
import supervision_2
import itertools
import debug
import drawing

class Test(WhiteboardWindow,threading.Thread):

    def __init__(self):

        WhiteboardWindow.__init__(self,defaultPeriod=0)        
        threading.Thread.__init__(self)
        self.daemon = True
        
    """Perform testing in different thread to allow for viewing progress of algorithms
    in real time."""
    def run(self):
    
        box = drawing.BoundingBox(25,75,30,70)
        triangles = [
            supervision_2.Triangle(Point(10,10),Point(90,10),Point(50,90))
        ]
        
        for triangle in triangles:
            triangle.draw(self)
            supervision_2.triangle_clipper(self,box,triangle)

t = Test()
t.start()
t.mainloop()
