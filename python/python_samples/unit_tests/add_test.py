#!/usr/bin/python

import unittest
from add import *

class TestMyClass(unittest.TestCase):

    def test_add(self):
        self.assertTrue( add(1,2) , 3)
        self.assertTrue( add(3,2) , 5)

if __name__ == '__main__':
    unittest.main()