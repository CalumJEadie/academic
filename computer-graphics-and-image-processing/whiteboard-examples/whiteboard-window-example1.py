#! /usr/bin/python

from Whiteboard import Point
from WhiteboardWindow import *

ww = WhiteboardWindow()

ww.draw(Point(10,10))

for x in range(50,60):
    for y in range(50,60):
        ww.draw(Point(x,y))

ww.mainloop()
