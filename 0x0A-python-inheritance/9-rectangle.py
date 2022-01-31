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

    def area(self):
        """
        Returns the rectangle area
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        Returns str with represents the rectangle
        """
        return "[{}] {}/{}".format(
            self.__class__.__name__, self.__width, self.__height)
