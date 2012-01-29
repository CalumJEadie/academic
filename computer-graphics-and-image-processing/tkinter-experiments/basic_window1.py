#! /usr/bin/python

"""
http://www.pythonware.com/library/tkinter/introduction/
"""

from Tkinter import *

root = Tk() # root widget
w = Label(root,text="hello!!!")
w.pack() # fits label widget to text size and becomes visibe
root.mainloop() # main loop - handles user input, windowing system events and queued graphical updates from tk
