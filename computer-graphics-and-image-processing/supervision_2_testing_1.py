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
    
        colours = itertools.cycle(["red","blue","green"])
    
        ps = [
            supervision_2.Polygon([Point(5,5),Point(40,5),Point(20,50)]),
            supervision_2.Polygon([Point(50,20),Point(70,40),Point(10,50)]),
            supervision_2.Polygon([Point(10,10),Point(20,10),Point(60,40),Point(40,70)]),
            supervision_2.Polygon([Point(30,30),Point(50,70),Point(20,90),Point(10,50)]),
            supervision_2.Polygon([Point(50,10),Point(70,10),Point(60,30),Point(40,70)])
        ]

        for p in ps:
            p.draw(self,colour=colours.next())
            debug.pause()
            supervision_2.fill(self,p,colour=colours.next())
            debug.pause()

t = Test()
t.start()
t.mainloop()
