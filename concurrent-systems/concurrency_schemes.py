"""
Implementation of Concurrency Schemes for Concurrent Systems.
http://www.cl.cam.ac.uk/teaching/1112/ConcDisSys/
"""

import threading
import time

# Event Count and Sequencers

class EventCount():
    """
    Implementation of an Event Count using python Lock.
    Python Lock is lowest level synchonisation primitive.
    """
    
    def __init__(self):
        
        self.count = 0
        self.lock = threading.Lock()
    
    def advance(self):
        
        self.lock.acquire()
        count = self.count # Create copy to make sure value returned is only incremented once.
        self.count += 1
        self.lock.release()
        count += 1
        return count
        
    def read(self):
        
        return self.count
        
    def await(self,v):
        """
        Performs busy wait on condition.
        
        How can this be implemented without busy wait?
        
        Could be implemented with a priority queue of blocked threads with the value they are waiting for. Use many locks to implement block the threads? A low level implementation would not make
        use of an implementation of a lock and rather would implement directly.
        """
        
        while self.count < v:
           time.sleep(1)
           
class Sequencer():
    
    def __init__(self):
        
        self.count = 0
        
    def ticket(self):
        
        self.lock.acquire()
        count = self.count
        self.count += 1
        self.lock.release()
        return count
        
class Lock():
    """
    Implementation of a lock using an event count and sequencer.
    Not a realisatic implementation as the event counts and sequencer themselves
    use a lock however shows how it could be done if event counts and sequencer
    were implemented at a lower level.
    """
    
    def __init__(self):
        
        self.event_count = EventCount()
        self.sequencer = Sequencer()
        
    def lock(self):
        
        turn = self.sequencer.ticket()
        self.event_count.await(turn)
        
    def unlock(self):
        
        self.event_count.advance()