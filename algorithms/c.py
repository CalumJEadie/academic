#! /usr/bin/python

"""
Common functions library.
"""

import random

def p(name,exp):
    """Prints name and value of an expression."""
    print name + ": " + str(exp)

def gen_randomint_dist(n,l0,dl,u0,du):
    """
    Generates a list of random integers. The range of integers that a particular
    element is choosen from can be related to the size of the list.
    Initial lower bound l0 with change dl and initial upper bound u0 with change du.
    """
    
    return [random.randint(l0+i*dl,u0+i*du) for i in range(0,n)]
