import unittest
from cw1 import Queue

class TestQueue(unittest.TestCase):
    def test_pop_front(self):
        q = Queue()
        q.append(1)
        q.append(2)
        q.pop_front()
        self.assertEqual(q.peek(), 2)

    def test_pop_front_2(self):
        q = Queue()
        self.assertEqual(q.pop_front(), -1)

unittest.main()