#! /usr/bin/python

"""
Introduction to Algorithms (3rd Ed.) - Chapter 15.
"""

import random

def cut_rod(prices,n):
    """Precondition: prices is a list of prices where the ith element is the price
    of a length i rod. len(prices) > n unless 0. prices[0] is not used.
    """
    
    if n > 0 and len(prices) <= n: raise Exception("Precondition: len(prices) > n unless n=0")

    if n == 0:
        return 0
    q = prices[1] + cut_rod(prices,n-1)
    for i in range(2,n):
        q = max(q,prices[i] + cut_rod(prices,n-i))
    return q
    
def cut_rod_test():
    
    tests = [
        [[0,1],1],
        [[0,1,1],1],
        [[0,1,1],2],
        [[0,1,2,0],3],
        [[0,0.5,2,3,0,10,0],6],
        [[0,0.5,2,3,12,10,0],6],
        [[0,0.5,2,3,12,10,0,0],7],
        [gen_randomint_dist(10,0,0,0,1),9],
        [gen_randomint_dist(20,0,0,0,1),19]
#        [gen_randomint_dist(30,0,0,0,1),29]
 #       [gen_randomint_dist(40,0,0,0,1),39],
#        [gen_randomint_dist(50,0,0,0,1),49]
#        [gen_randomint_dist(100,0,0,0,1),99]
    ]
    for test in tests:
        ps = test[0]
        n = test[1]
        pn("ps",ps)
        pn("n",n)
        try:
            pn("best",cut_rod(ps,n))
        except Exception as e:
            pn("Error",e)
