#!/usr/bin/python3
"""how is it"""
import unittest

class TestEverything(unittest.TestCase):
    """This is just an example TestCase"""

    def test_upper(self):
        """First test baby"""
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    """not sure"""
    unittest.main()
