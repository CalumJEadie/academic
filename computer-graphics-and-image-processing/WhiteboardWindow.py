#! /usr/bin/python

from Whiteboard import *
from Tkinter import *
import threading
import time

"""Provides a window to draw to.
"""
class WhiteboardWindow(Tk):

    def __init__(self,width=100,height=100,scaling=4,defaultPeriod=0):
        
        Tk.__init__(self)
        self.whiteboard = Whiteboard(self,width,height,scaling)
        self.defaultPeriod = defaultPeriod
        
    def draw(self,point,period=None,colour=None):
    
        if period is None:
            period = self.defaultPeriod
            
        if colour is None:
            colour = "blue"
            
        time.sleep(period)
        self.whiteboard.draw(point,colour)
