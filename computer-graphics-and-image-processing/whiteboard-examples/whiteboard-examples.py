#! /usr/bin/python

from Whiteboard import *
from Tkinter import *

root = Tk()
w = Whiteboard(root,100,100,4)

for x in range(50,60):
    for y in range(50,60):
        w.draw(Point(x,y))
        
for i in range(10,90):
    w.draw(Point(i,2*i))
    
root.mainloop()
