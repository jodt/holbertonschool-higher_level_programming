#!/usr/bin/python3
"""
This is the square module
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class create a square
    """

    def __init__(self, size):
        """
        Initialize data

        Parameter
        ---------
        size (int) : size of the square
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
