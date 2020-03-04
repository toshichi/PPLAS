#!/usr/bin/python3

import sys
import unittest
from io import StringIO


class ProblemTest(unittest.TestCase):
    def setUp(self):
        self.captor = StringIO()
        sys.stdout = self.captor

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_main(self):
        import problem
        self.assertEqual(self.captor.getvalue(), 'Hello World!\n')


if __name__ == '__main__':
    unittest.main()