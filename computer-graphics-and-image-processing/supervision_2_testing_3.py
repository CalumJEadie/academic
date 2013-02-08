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

class Test(WhiteboardWindow,threading.Thread):

    def __init__(self):

        WhiteboardWindow.__init__(self,defaultPeriod=0)        
        threading.Thread.__init__(self)
        self.daemon = True
        
    """Perform testing in different thread to allow for viewing progress of algorithms
    in real time."""
    def run(self):
    
        colours = itertools.cycle(["red","blue","green","purple","orange","yellow"])
            
        boundingPolygon = supervision_2.Polygon([Point(20,20),Point(70,30),Point(80,80),Point(30,70)])
        boundingPolygon.draw(self,colour=colours.next())
        
        ps = [
            supervision_2.Polygon([Point(10,10),Point(50,90),Point(90,10)]),
            supervision_2.Polygon([Point(10,20),Point(50,50),Point(90,10)]),
            supervision_2.Polygon([Point(11,11),Point(91,11),Point(51,91)]), # interesting, order of vertices does not seem to matter?
            supervision_2.Polygon([Point(5,40),Point(95,30),Point(96,60),Point(60,70)]),
            supervision_2.Polygon([Point(15,15),Point(50,15),Point(50,50),Point(30,30),Point(20,50)])
        ]
        
        for p in ps:
            colour=colours.next()
            p.draw(self,colour)
            debug.pause()
            supervision_2.sutherland_hodgman_clipper(self,boundingPolygon,p,colour)
            debug.pause()

t = Test()
t.start()
t.mainloop()
