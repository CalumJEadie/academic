#!/usr/bin/env python

import games
from graph import *

t = Tree(None,[
    Tree(None,[
        Tree(None,[
            Tree(None,[
                Tree(1),
                Tree(-15)
            ]),
            Tree(None,[
                Tree(2),
                Tree(19)
            ])
        ]),
        Tree(None,[
            Tree(None,[
                Tree(18),
                Tree(23)
            ]),
            Tree(None,[
                Tree(4),
                Tree(3)
            ])
        ]),
    ]),
    Tree(None,[
        Tree(None,[
            Tree(None,[
                Tree(2),
                Tree(1)
            ]),
            Tree(None,[
                Tree(7),
                Tree(8)
            ])
        ]),
        Tree(None,[
            Tree(None,[
                Tree(9),
                Tree(10)
            ]),
            Tree(None,[
                Tree(-2),
                Tree(5)
            ])
        ]),
    ]),
    Tree(None,[
        Tree(None,[
            Tree(None,[
                Tree(-1),
                Tree(-30)
            ]),
            Tree(None,[
                Tree(4),
                Tree(7)
            ])
        ]),
        Tree(None,[
            Tree(None,[
                Tree(20),
                Tree(-1)
            ]),
            Tree(None,[
                Tree(-1),
                Tree(5)
            ])
        ])
    ])
])

def label(node,parent_label,position):
    """
    Add hierachial labels to tree.
    """
    
    node.l = parent_label + str(position)
    
    i = 0
    for child in node.children:
        label(child,node.l,i)
        i += 1
            
label(t,"",0)

print str(t)
print games.alpha_beta_pruning_search(t)