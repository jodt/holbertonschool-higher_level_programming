#!/usr/bin/python3
"""
This is the "max_interger_test" module.

The max_integer_test module supplies a class to test max_integer function
"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        """
        Test function with list of integer
        """
        self.assertEqual(max_integer([5, 7, 9]), 9)
        self.assertEqual(max_integer([-6, 7, 9]), 9)
        self.assertEqual(max_integer([9, 7, 3]), 9)
        self.assertEqual(max_integer([2, 9, 3]), 9)
        self.assertEqual(max_integer([-9, -5, -4]), -4)
        self.assertEqual(max_integer([9]), 9)
        self.assertEqual(max_integer([]), None)
