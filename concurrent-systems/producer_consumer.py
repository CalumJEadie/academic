"""
Implementation of Producer-Consumer using different concurrency methods.
"""

import threading
import urllib2
import random
from BeautifulSoup import BeautifulSoup
import time
import concurrency_schemes

# Producer and Consumer

XKCD_URL = "http://www.xkcd.com/%s/"

class Producer(threading.Thread):
    
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue
    
    def produce(self):
        """
        Produces HTML for an arbitary xkcd comic.
        
        Returns (comic_num,html).
        """
        
        comic_num = random.randint(1,1000)
        html = urllib2.urlopen(XKCD_URL % comic_num).read()
        return (comic_num,html)
        
    def run(self):
        while True:
            item = self.produce()
            self.queue.put(item)
        
class Consumer(threading.Thread):
    
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue
    
    def consume(self,comic_num,html):
        """
        Consumes HTML from an xkcd comic and outputs comic title.
        """
        
        soup = BeautifulSoup(html)
        title = soup.title.string
        print "%s: \"%s\"" % (comic_num,title)
        
    def run(self):
        while True:
            (comic_num,html) = self.queue.get()
            self.consume(comic_num,html)
            
# Unsafe Implementation

class UnsafeQueue():
    
    def __init__(self,maxsize):
        
        self.queue = [0]*maxsize
        self.head = 0
        self.tail = 0
        
    def put(self,item):
        
        print "put(%s)" % str(item)[0:50]
        
        self.queue[self.tail] = item
        self.tail = (self.tail+1) % len(self.queue)
        
    def get(self):
        
        item = self.queue[self.head]
        self.head = (self.head+1) % len(self.queue)
        
        print "get() = %s" % str(item)[0:50]
        return item

# Semaphore Implementation

class SemaphoreQueue():
    
    def __init__(self,maxsize):
        
        self.queue = [0]*maxsize
        self.head = 0
        self.tail = 0
        self.spaces = threading.Semaphore(maxsize)
        self.items = threading.Semaphore(0)
        self.guard = threading.Semaphore(1)
        
    def put(self,item):
        print "put(%s)" % str(item)[0:50]
        
        self.spaces.acquire() # Wait until spaces available ( Condition sychronisation ).
        self.guard.acquire() # Wait until can modify the queue ( Mutual exclusion ).
        self.queue[self.tail] = item
        self.tail = (self.tail+1) % len(self.queue)
        self.guard.release()
        self.items.release()
        
    def get(self):
        self.items.acquire()
        self.guard.acquire()
        item = self.queue[self.head]
        self.head = (self.head+1) % len(self.queue)
        self.guard.release()
        self.spaces.release()
        
        print "get() = %s" % str(item)[0:50]
        return item
        
# Event Counte Implementation

class EventCountQueue():
    
    def __init__(self,maxsize):
        
        self.queue = [0]*maxsize
        
        # Achieve mutual exclusion of head and tail using sequences.
        self.pev = EventCount()
        self.psq = Sequencer()
        self.gev = EventCount()
        self.gsq = Sequencer()
        
    def put(self,item):
        print "put(%s)" % str(item)[0:50]
        
        turn = self.psq.ticket()
        # Achieve mutual exclusion so each put writes to different part of the queue.
        self.pev.await(turn)
        # Wait until space available at the part of the queue assigned to the callee.
        self.cev.await((turn-len(self.queue))+1)
        self.queue[turn % len(self.queue)] = item
        self.pev.advance()
        
    def get(self):
        
        turn = self.csq.ticket()
        self.cev.await(turn)
        # Wait until one more put than get has taken place.
        self.pev.await(turn+1)
        item = self.queue[turn % len(self.queue)]
        self.cev.advance()
        
        print "get() = %s" % str(item)[0:50]
        return item

# Monitor Implementation

class MonitorQueue(Lock):
    
    def __init__(self,maxsize):
        
        Lock.__init__(self)
        
        self.queue = [0]*maxsize
        
        # Achieve mutual exclusion of head and tail using lock on self.
        self.head = 0
        self.tail = 0
        
        self.notfull = Condition()
        self.notempty = Condition()
        
    def put(self,item):
        print "put(%s)" % str(item)[0:50]
        
        self.acquire() # Achieve mutual exclusion over queue, head and tail by locking on self.
        self.notfull.acquire()
        if self.tail-self.head == len(self.queue): # Would need to consider subtraction % N for working implementation.
            self.notfull.wait()
            
        self.queue[self.tail % n] = item
        self.tail += 1
        self.notempty.signal()
        self.release()