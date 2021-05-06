#!/usr/bin/python3

import sys
import unittest
import contextlib
from io import StringIO


class redirect_stdin(contextlib._RedirectStream):
    _stream = "stdin"


class ProblemTest(unittest.TestCase):
    def test_input(self):
        import problem

    def test_main(self):
        self.captor = StringIO()
        self.sender = StringIO()
        self.sender.write("Input content\n")
        self.sender.seek(0)
        with contextlib.redirect_stdout(self.captor), redirect_stdin(self.sender):
            self.test_input()
        actual = self.captor.getvalue()
        print(actual)
        expected = "Input text here:\nWhat you input was: Input content\n"
        # self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
