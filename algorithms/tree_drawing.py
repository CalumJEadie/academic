"""
Provides tree drawing.
"""

from collections import deque
from graph import Node,Edge

def draw(tree):
    """Draws `tree`. `tree` is assumed to be acyclic.
    """
    
    if not isinstance(tree,Node):
        raise TypeError("tree in draw(tree) must be an instance of Node.")
        
def printTree(tree):
    """Prints `tree`. `tree` is assumed to be acyclic.
    """
    
    if not isinstance(tree,Node):
        raise TypeError("tree in print(tree) must be an instance of Node.")
        
    # Breadth first search of tree.
    
    nodesQueue = deque([tree])
    
    while len(nodesQueue) > 0:
    
        currNode = nodesQueue.popleft()
        
        numEdges = len(currNode.edges)
        
        print currNode
        
        for edge in currNode.edges:
            print edge
            nodesQueue.append(edge.dest)
