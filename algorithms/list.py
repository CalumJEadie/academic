"""
Implementations of list data structures and algorithms that use them.
"""

class LinkedList():
    """
    A linked list implementing a subset of python "list" behavoir.
    """
    
    head = None;
    tail = None;
    
    def __add__(self,list):
        
        a = self.copy()
        b = list.copy()
        a.tail.next = b.head
        return a.copy()
        
    def __contains__(self,value):
        
        for i in self:
            if i == value:
                return True
        return False
    
    def __init__(self,values):
        """
        Construct LinkedList using values array.
        """
        
        if len(values) >= 1:
            self.head = Node(values[0])
            self.tail = self.head
        
        for value in values[1:]:
            self.append(value)
            
    def __iter__(self):
        """
        Returns an iterator object implemented using a generator method.
        http://docs.python.org/library/stdtypes.html#iterator-types
        """
        
        for node in self._node_iter():
            yield node.value
        
    def __str__(self):
        
        return ','.join(str(i) for i in self)
            
    def append(self,value):
        
        if self.tail == None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
            
    def copy(self):
        """
        Returns a shallow copy.
        """
        
        list = LinkedList([])
        for i in self:
            list.append(i)
        return list
        
    def delete(self,value):
        """
        Deletes first node with value specified.
        """
        
        prev = None
        
        for node in self._node_iter():
            if node.value == value:
                if node == self.head:
                    self.head = node.next
                else:
                    prev.next = node.next
                    
                if node == self.tail:
                    self.tail = prev
                    
                break
            prev = node
            
    def _node_iter(self):
        """
        Returns an iterator object over the underlying representation of values.
        """
        
        next = self.head
        
        while next != None:
            yield next
            next = next.next
            
        raise StopIteration
        
class DoublyLinkedList(LinkedList):
    
    def __add__(self,list):
        
        a = self.copy()
        b = list.copy()
        a.tail.next = b.head
        b.head.prev = a.tail
        return a.copy()
    
    def __init__(self,values):
        
        LinkedList.__init__(self,values)
        
    def __reversed__(self):
        
        for node in self._node_revered():
            yield node.value
            
    def append(self,value):
        
        if self.tail == None:
            self.head = Node(value)
            self.tail = self.head
        else:
            node = Node(value)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            
    def _node_revered(self):
        """
        Returns an iterator object over the underlying representation of values
        that iterates in reverse.
        """
        
        prev = self.tail
        
        while prev != None:
            yield prev
            prev = prev.prev
            
        raise StopIteration
        
    def delete(self,value):
        """
        Deletes first node with value specified.
        """
        
        prev = None
        
        for node in self._node_iter():
            if node.value == value:
                if node == self.head:
                    self.head = node.next
                else:
                    prev.next = node.next
                    
                if node == self.tail:
                    self.tail = prev
                else:
                    node.next.prev = prev
                    
                break
            prev = node

class Node():
    
    value = None
    next = None
    prev = None
    
    def __init__(self,value):
        
        self.value = value