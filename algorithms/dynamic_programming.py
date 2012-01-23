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
    
def memoized_cut_rod(prices,n):
    """cut_rod using a top down memoization approach.
    """
    
    r = [False] * (n+1) # use False to denote unknown
    return memoized_cut_rod_aux(prices,n,r)
    
def memoized_cut_rod_aux(prices,n,r):
    
    if r[n] != False:
        return r[n]
        
    if n == 0:
        q = 0
    else:
        q = prices[1] + memoized_cut_rod_aux(prices,n-1,r)
        for i in range(2,n):
            q = max(q,prices[i] + memoized_cut_rod_aux(prices,n-i,r))
    r[n] = q # record value, this is where "memo" comes from
    return q
