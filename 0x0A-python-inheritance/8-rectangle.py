#!/usr/bin/python3
"""
This is the rectangle module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class create a rectangle
    """

    def __init__(self, width, height):
        """
        Initialize data

        Parameters
        ----------
        width (int) : with of the rectangle
        height (int) : height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
