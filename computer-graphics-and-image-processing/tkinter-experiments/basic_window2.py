#! /usr/bin/python

"""
http://www.pythonware.com/library/tkinter/introduction/hello-again.htm
"""

from Tkinter import *

class App:

    def __init__(self,master):
    
        frame = Frame(master) # create frame widget
        frame.pack() # make frame visible
        
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit) # add button widget
        self.button.pack(side=LEFT)
        
        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)
        
        # http://www.pythonware.com/library/tkinter/introduction/x131-more-on-widget-references.htm
        # widgets retain reference to their parent widget

    def say_hi(self):
        print "hi there, everyone!"

root = Tk() # create root widget

app = App(root)

root.mainloop()
