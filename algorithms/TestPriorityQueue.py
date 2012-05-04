#! /usr/bin/env python

import unittest
import priority_queue

class TestPriorityQueue(unittest.TestCase):
    
    queues = []
    
    def setUp(self):
        
        items = [
            priority_queue.Item(1,'apples'),
            priority_queue.Item(2,'bananas'),
            priority_queue.Item(3,'elderflowers')
        ]
        self.queues.append(
            priority_queue.PriorityQueueList(items)
        )
        
    def test_str(self):
        
        for q in self.queues:
            print str(q)
            
    def test_insert(self):
        
        for q in self.queues:
            q.insert(Item(4,'grapes'))
            expected = '[Item(1,apples), Item(2,bananas), Item(3,elderflowers),Item(4,grapes)]'
            self.assertEqual(expected,repr(q))
            
    def test_first(self):
        
        for q in self.queues:
            first = q.first()
            expected = 'Item(1,apples)'
            self.assertEqual(expected,repr(first))
            
    def test_extract_min(self):
        
        for q in self.queues:
            min = q.extract_min()
            expected = 'Item(1,apples)'
            self.assertEqual(expected,repr(first))
            expected = '[Item(2,bananas), Item(3,elderflowers)]'
            self.assertEqual(expected,repr(q))
            
    def test_decrease_key(self):
        
        for q in self.queues:
            first = q.first()
            q.decrease_key(first,-1)
            expected = '[Item(-1,apples), Item(2,bananas), Item(3,elderflowers)]'
            self.assertEqual(expected,repr(q))
            
    def test_delete(self):
        
        for q in self.queues:
            first = q.first()
            q.delete(first)
            expected = '[Item(2,bananas), Item(3,elderflowers)]'
            self.assertEqual(expected,repr(q))
        
    def tearDown(self):
        
        self.queues = []
    
if __name__ == '__main__':

    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPriorityQueue)
    unittest.TextTestRunner(verbosity=2).run(suite)