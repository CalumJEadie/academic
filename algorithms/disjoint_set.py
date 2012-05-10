class DisjointSetCollection_PythonSet()
    """
    Implemementation of Disjoint Sets data structure using Python sets.
    """

    sets = []
    
    def make_set(self,x):
        assert self.find_set(x) == False
        sets.append(set([x]))
        
    def find_set(self,x):
        for set in self.sets:
            if x in set:
                return set
        return False
        
    def union(self,x,y):
        set_x = self.find_set(x)
        set_y = self.find_set(y)
        assert set_x != False
        assert set_y != False
        assert set_x != set_y
        assert set_x.isdisjoint(set_y)
        set_x = set_x.union(set_y)
        self.sets.remove(set_x)
        
class DisjointSetsCollection_Forest()
    """
    Implementation of Disjoint Sets data structure using a forest
    of trees and using path compression and union by rank heuristics.
    """
    
    sets = []
    
    def make_set(x):
        """
        Assumes x not in self.
        """
        
        x.parent = x
        x.rank = 0
        self.sets.append(x)
    
    def find_set(self,x):
        """
        Assumes x in self.
        """
        
        # Test if x is root of a tree
        if x != x.parent:
            # Find root of x and compress paths at same time.
            x.p = self.find_set(x.p)
        return x.p
        
    def union(self,x,y):
        """
        Assumes x and y in self.
        """
        
        xp = self.find_set(x)
        yp = self.find_set(y)
        
        if xp.rank > yp.rank:
            yp.p = xp
        elif xp.rank < yp.rank:
            xp.p = yp
        else:
            xp.p = yp
            yp.rank += 1