#!/usr/bin/env python

"""Towers of Hanoi"""

import math

class Game():

    tower_a = None
    tower_b = None
    tower_c = None
    
    def __init__(self,n):
    
        self.tower_a = Tower(n)
        self.tower_b = Tower(0)
        self.tower_c = Tower(0)
    
    def move(self,source_tower,n,dest_tower):
    
        if n < 0:
            raise ValueError("Number of rings, n must be >= 0.")
        elif n == 1:
            if( len(dest_tower) > 0 and source_tower[-1] >= dest_tower[-1] ):
                raise IllegalMoveError(self,source_tower,dest_tower)
            else:
                dest_tower.append(source_tower.pop())
        else:
            work_tower = self.get_work_tower(source_tower,dest_tower)
            self.move(source_tower,n-1,work_tower)
            self.move(source_tower,1,dest_tower)
            self.move(work_tower,n-1,dest_tower)
            
    def stepped_move(self,source_tower,n,dest_tower):
        print self
    
        self._stepped_move(source_tower,n,dest_tower,1)
    
    def _stepped_move(self,source_tower,n,dest_tower,step):
        
        if n < 0:
            raise ValueError("Number of rings, n must be >= 0.")
        elif n == 1:
            if( len(dest_tower) > 0 and source_tower[-1] >= dest_tower[-1] ):
                raise IllegalMoveError(self,source_tower,dest_tower)
            else:
                dest_tower.append(source_tower.pop())
                
                print "\n-- step %s -->" % step
                print "\n"+str(self)
        else:
            work_tower = self.get_work_tower(source_tower,dest_tower)
            step = self._stepped_move(source_tower,n-1,work_tower,step+1)
            step = self._stepped_move(source_tower,1,dest_tower,step+1)
            step = self._stepped_move(work_tower,n-1,dest_tower,step+1)
            
        return step
            
    def move_a_b(self,n,stepped=True):
        if stepped:
            self.stepped_move(self.tower_a,n,self.tower_b)
        else:
            self.move(self.tower_a,n,self.tower_b)
    def move_a_c(self,n,stepped=True):
        if stepped:
            self.stepped_move(self.tower_a,n,self.tower_c)
        else:
            self.move(self.tower_a,n,self.tower_c)
    def move_b_a(self,n,stepped=True):
        if stepped:
            self.stepped_move(self.tower_b,n,self.tower_a)
        else:
            self.move(self.tower_b,n,self.tower_a)
    def move_b_c(self,n,stepped=True):
        if stepped:
            self.stepped_move(self.tower_b,n,self.tower_c)
        else:
            self.move(self.tower_b,n,self.tower_c)
    def move_c_a(self,n,stepped=True):
        if stepped:
            self.stepped_move(self.tower_c,n,self.tower_a)
        else:
            self.move(self.tower_c,n,self.tower_a)
    def move_c_c(self,n,stepped=True):
        if stepped:
            self.stepped_move(self.tower_c,n,self.tower_b)
        else:
            self.move(self.tower_c,n,self.tower_b)
    
    def get_work_tower(self,source,dest):
        """Determines which tower is the work tower given source and dest."""
        
        for tower in [self.tower_a,self.tower_b,self.tower_c]:
            if tower is not source and tower is not dest:
                return tower
                
    def __str__(self):
    
        height_a = len(self.tower_a)
        height_b = len(self.tower_b)
        height_c = len(self.tower_c)
        height_max = max(height_a,height_b,height_c)
        
        width_a = Game._width(height_a)
        width_b = Game._width(height_b)
        width_c = Game._width(height_c)
        
        s = []
        for i in reversed(range(0,height_max)):
        
            if i < height_a:
                s.append(Game._ring_str(self.tower_a[i],width_a))
            else:
                s.append(" "*(width_a+2))
                
            s.append(" ")
        
            if i < height_b:
                s.append(Game._ring_str(self.tower_b[i],width_b))
            else:
                s.append(" "*(width_b+2))
                
            s.append(" ")
        
            if i < height_c:
                s.append(Game._ring_str(self.tower_c[i],width_a))
            else:
                s.append(" "*(width_c+2))
                
            s.append("\n")
        
        s.append("-"*(width_a+width_b+width_c+9)+"\n")
        s.append("%s %s %s" % ("A".center(width_a+2),"B".center(width_b+2),"C".center(width_c+2)))
        
        return "".join(s)
            
    @staticmethod
    def _width(height):
        return int(math.ceil(math.log10(height+1)))
        
    @staticmethod
    def _ring_str(n,width):
        return "[%s]" % str(n).center(width)
        
class Tower(list):
    """Lowest ring stored at position 0."""

    def __init__(self,n):
    
        super(Tower,self).__init__(range(1,n+1))
        self.reverse()
    
    def __str__(self):
    
        s = []
        for ring in reversed(self):
            s.append("[ %s ]" % ring)
        return "\n".join(s)
        
class Error(Exception):
    """Base class for exceptions in this module."""
    pass
    
class IllegalMoveError(Exception):
    
    game = None
    source_tower = None
    dest_tower = None
    
    def __init__(self,game,source_tower,dest_tower):
        self.game = game
        self.source_tower = source_tower
        self.dest_tower = dest_tower
        
    def __str__(self):
        return "Move,\n\n%s\n\n--->\n\n%s\n\nin game,\n\n%s" % (self.source_tower,self.dest_tower,self.game)

################################################################################
# Control logic

def main():
    
    print "/"+"-"*78+"\\"
    print "|"+"Towers of Hanoi".center(78)+"|"
    print "\\"+"-"*78+"/"
    
    while True:
        response = raw_input("\nEnter tower size or Q to quit: ")
        
        if response.upper() == "Q":
            break
        else:
            try:
                n = int(response)
                g = Game(n)
            except ValueError:
                continue
                
            print str(g)
                
            while True:
                source = select_tower(g,raw_input("\nSource (A,B,C): "))
                dest = select_tower(g,raw_input("Destination (A,B,C): "))
                
                g.move(source,1,dest)
                print "\n"+str(g)
                
                if len(g.tower_c) == n:
                    print "\nSolved!"
                    break
                
def select_tower(game,response):

    towers = {
        "A": game.tower_a,
        "B": game.tower_b,
        "C": game.tower_c
    }
    return towers[response.upper()]
    
if __name__ == '__main__':
    main()
