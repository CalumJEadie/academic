"""
Collection of debug utilities.
"""

def pause():
    raw_input("Execution Paused (enter to resume).")
    
def printl(items):
    for item in items:
        print item
