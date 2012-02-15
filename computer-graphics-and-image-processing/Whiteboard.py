#! /usr/bin/python

"""Copyright (c) 2012 Calum J. Eadie <www.calumjeadie.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

"""Follows Tkinter design pattern as using classes that are widgets rather than
creating high level object that would not be embeddable.

http://www.pythonware.com/library/tkinter/introduction/canvas.htm
http://effbot.org/tkinterbook/canvas.htm"""

from Tkinter import *

"""Responsible for representing points on the whiteboard or canvas.
"""
class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "Point({0},{1})".format(self.x,self.y)
        
    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)
        
    def __mul__(self,factor):
        # http://docs.python.org/reference/datamodel.html
        if isinstance(factor,int) or isinstance(factor,float):
            return Point(self.x*factor,self.y*factor)
        else:
            return NotImplemented
            
    __rmul__ = __mul__
    
    @staticmethod
    def fromPoint(point):
        return Point(point.x,point.y)

"""Provides a widget with basic drawing capabilities. Coordinate system has origin at bottom left.
"""
class Whiteboard(Canvas):

    def __init__(self,master,width,height,scaling):
    
        self.wwidth = width
        self.wheight = height
        self.scaling = scaling # relationship between whiteboard and canvas coordinate systems
        
        self.cwidth = width*scaling
        self.cheight = height*scaling
    
        Canvas.__init__(self,master,width=self.cwidth,height=self.cheight)
        
        self.pack(fill=BOTH,expand=YES)
        
    def printOutOfRangeErr(self,point0,point1):
        print "Out of range: {0} -> {1}".format(point0,point1)
    
    """Get canvas point from whiteboard point.
    """
    def getCPoint(self,point):
    
        wpoint = Point.fromPoint(point)
    
        outOfRange = False
        if wpoint.x < 0:
            outOfRange = True
            wpoint.x = 0
        elif wpoint.x >= self.wwidth:
            outOfRange = True
            wpoint.x = self.wwidth-1
            
        if wpoint.y < 0:
            outOfRange = True
            wpoint.y = 0
        elif wpoint.y >= self.wheight:
            outOfRange = True
            wpoint.y = self.wheight-1
            
        if outOfRange:
            self.printOutOfRangeErr(point,wpoint)
    
        cpoint = Point(wpoint.x*self.scaling,self.cheight-(wpoint.y*self.scaling))
        return cpoint
        
    def draw(self,wpoint,colour):
    
        cpoint = self.getCPoint(wpoint)
        self.create_rectangle(cpoint.x,cpoint.y,cpoint.x+self.scaling,cpoint.y-self.scaling,outline=colour,fill=colour)
