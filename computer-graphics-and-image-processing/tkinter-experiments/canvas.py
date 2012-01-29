#! /usr/bin/python

"""
http://www.pythonware.com/library/tkinter/introduction/canvas.htm
"""

from Tkinter import *

def draw(canvas,x,y):
    canvas.create_line(x,y,x+1,y+1)

root = Tk()
root.title("Canvas")
canvas = Canvas(root, width=200, height=200)
canvas.pack()

canvas.create_line(100,100,105,105, width=2)
for x in range(40,350):
    draw(canvas,x,200)

root.mainloop()
