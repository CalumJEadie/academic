#! /usr/bin/python

from Whiteboard import Point
from WhiteboardWindow import *
import threading
import time

ww = WhiteboardWindow(defaultPeriod=0.05)

def draw():

    for x in range(50,60):
        for y in range(50,60):
            ww.draw(Point(x,y))
            
t = threading.Thread(target=draw)
t.daemon = True
t.start()

ww.mainloop()
