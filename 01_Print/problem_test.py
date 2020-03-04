#!/usr/bin/python3

import sys
import unittest
import contextlib
from io import StringIO


class ProblemTest(unittest.TestCase):
    def test_output(self):
        import problem

    def test_main(self):
        self.captor = StringIO()
        with contextlib.redirect_stdout(self.captor):
            self.test_output()
        actual = self.captor.getvalue()
        expected = 'Hello World!\n'
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()