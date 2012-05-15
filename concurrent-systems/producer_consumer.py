"""
Implementation of Producer-Consumer using different concurrency methods.
"""

import threading
import urllib2
import random
from BeautifulSoup import BeautifulSoup
import time

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
        
# Event Counter Implementation

# Monitor Implementation