#! /usr/bin/python

import unittest

import tree_drawing
from graph import *
import itertools
import random

class TestTreeDraw(unittest.TestCase):
    
    nodeGenerator = itertools.imap(lambda x: Node([]),itertools.count(0))
            
    @staticmethod
    def generateValue():
        return random.randint(1,20)

    def setUp(self):
        self.tree = self.nodeGenerator.next()
        
    def tearDown(self):
        pass
        
    def test_print1(self):
        tree_drawing.printTree(self.tree)
        
    def test_print2(self):
    
        # Extend tree    
        for i in range(0,2):
            n = self.nodeGenerator.next()
            self.tree.edges.append(Edge(self.tree,n,TestTreeDraw.generateValue()))
            
        tree_drawing.printTree(self.tree)
    
if __name__ == "__main__":

    #unittest.main()
#    suite = unittest.TestLoader().loadTestsFromTestCase(TestTreeDraw)
#    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestSuite()
#    suite.addTest(TestTreeDraw('test_print1'))
    suite.addTest(TestTreeDraw('test_print2'))
    unittest.TextTestRunner(verbosity=2).run(suite)
