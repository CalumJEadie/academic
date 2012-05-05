class DisjointSetCollection()

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