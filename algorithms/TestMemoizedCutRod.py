#! /usr/bin/python

import random
import unittest
from c import *
import time

import dynamic_programming

class TestMemoizedCutRod(unittest.TestCase):

    def test_small(self):
    
        tests = [
            [[0,1],1],
            [[0,1,1],1],
            [[0,1,1],2],
            [[0,1,2,0],3],
            [[0,0.5,2,3,0,10,0],6],
            [[0,0.5,2,3,12,10,0],6],
            [[0,0.5,2,3,12,10,0,0],7]
        ]
        for test in tests:
            self.do_test(test[0],test[1])
            
    def test_large(self):
    
        tests = [[gen_randomint_dist(n+1,0,0,0,1),n] for n in range (15,25)]
        for test in tests:
            self.do_test(test[0],test[1])
            
    def test_vlarge(self):
    
        tests = [[gen_randomint_dist(n+1,0,0,0,1),n] for n in range (25,45)]
        for test in tests:
            self.do_test(test[0],test[1])
            
    def do_test(self,ps,n):
    
        p("ps",ps)
        p("n",n)
        try:
            # Use system time over timeit, less accurate but can get at result.
            #t = timeit.Timer(stmt="best = dynamic_programming.cut_rod(ps,n)", setup="import dynamic_programming")
            t1 = time.clock()
            p("best",dynamic_programming.memoized_cut_rod(ps,n))
            t2 = time.clock()
            p("dt",t2-t1)
        except Exception as e:
            p("Error",e)
        print
    
if __name__ == "__main__":

    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMemoizedCutRod)
    unittest.TextTestRunner(verbosity=2).run(suite)
