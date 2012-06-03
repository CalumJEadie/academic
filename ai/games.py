from graph import *

INF = float('inf')
NINF = float('-inf')

def piv(s,n,verbose):
    """
    Print if verbose, helper method to so prevent debugging reducing clarity of
    algorithms.
    """
    if verbose:
        print (" %s ---> %s " % (n.l,s)).center(80,"-")
    return s

def alpha_beta_pruning_search(root,verbose=True):
    """
    Implementation of Alpha Beta Pruning which performs minimax using reasoning about the other
    players moves to avoid exploring parts of the tree.
    
    Max moves first. Largest outcome best for Max.
    
    alpha = highest seen on Max's best path
    beta = lowest on Min's best path
    """
    
    def player(alpha,beta,n,verbose=True):
        if verbose:
            print (" player(%s,%s,%s) " % (alpha,beta,n.l) ).center(80,"-")
            print n
        
        if len(n.children) == 0:
            return piv(n.v,n,verbose)
        else:
            value = NINF
            for child in n.children:
                value = max(value,opponent(alpha,beta,child))
                if value > beta:
                    return piv(value,n,verbose)
                if value > alpha:
                    alpha = value
            return piv(value,n,verbose)
        
    def opponent(alpha,beta,n,verbose=True):
        if verbose:
            print (" opponent(%s,%s,%s) " % (alpha,beta,n.l) ).center(80,"-")
            print n
        
        if len(n.children) == 0:
            return piv(n.v,n,verbose)
        else:
            value = INF
            for child in n.children:
                value = min(value,player(alpha,beta,child))
                if value < alpha:
                    return piv(value,n,verbose)
                if value < beta:
                    beta = value
            return piv(value,n,verbose)
        
    return player(NINF,INF,root,verbose)