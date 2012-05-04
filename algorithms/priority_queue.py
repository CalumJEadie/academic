class PriorityQueueList(list):
    """
    Implementation of a priority queue using a python list.
    Algorithms II - Chapter I - Advanced Data Structures
    """
    
    def __init__(self,items):
        list.__init__(self,items)
        self.sort()
        
    def insert(self,item):
        self.append(item)
        self.sort()
        
    def first(self):
        return self[0].value
        
    def extract_min(self):
        min = self[0].value
        del self[0]
        return min
        
    def decrease_key(self,item,new):
        for i in self:
            if i == item:
                item.key = new
                break
                
    def delete(self,item):
        remove(item)
        
class Item():
    
    key = None
    value = None
    
    def __init__(self,key,value):
        
        self.key = key
        self.value = value
        
    def __cmp__(self,other):
        
        return cmp(self.key,other.key)
        
    def __repr__(self):
        
        return "Item(%s,%s)" % (self.key,self.value)