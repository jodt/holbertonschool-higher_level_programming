#!/usr/bin/python3
"""
This is the MyInt module
"""


class MyInt(int):
    """
    Create a MyInt class
    """

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if self.value == other:
            return False

    def __ne__(self, other):
        if self.value == other:
            return True
