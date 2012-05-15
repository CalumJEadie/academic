#!/usr/bin/env python

import unittest
import producer_consumer
import time

class Test(unittest.TestCase):
    
    def do_test(self,queue):
        
        for i in range(0,5):
            p = producer_consumer.Producer(queue)
            p.daemon = True
            p.start()
            
        for i in range(0,2):
            c = producer_consumer.Consumer(queue)
            c.daemon = True
            c.start()
            
        time.sleep(30)
    
    #def test_unsafe(self):
        #queue = producer_consumer.UnsafeQueue(5)
        #self.do_test(queue)
    
    def test_semaphore(self):
        queue = producer_consumer.SemaphoreQueue(5)
        self.do_test(queue)
    
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)