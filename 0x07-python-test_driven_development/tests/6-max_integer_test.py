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
        self.assertEqual(max_integer([]), None)

    def test_type(self):
        """
        Test Raises
        """
        self.assertRaises(TypeError, max_integer, "salut")
        self.assertRaises(TypeError, max_integer, [3.5, 7, 9])
        self.assertRaises(TypeError, max_integer, ["hello", 7, 9])
        self.assertRaises(TypeError, max_integer, -5)
