#!usr/bin/python3
"""
This module create a rectangle
"""


class Rectangle:
    """
    This class represents a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initialise data

        Parameters
        ----------
        width (int) : width of the  rectangle
        height (int) : heigth of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter to access of the width value

        Return
            ------
         int : value of width
            """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter to update width value

        Parameter:
        ----------
        Value (int): value of width

        Raises
        ------
        TypeError: if value is not integer
        ValueError: if value is < 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter to access of the heigth value

        Return
        ------
        int : value of heigth
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter to update height value

        Parameter:
        ----------
        Value (int): value of height

        Raises
        ------
        TypeError: if value is not integer
        ValueError: if value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Return the aera of the rectangle

        Return:
        -------
        int: the aera of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter of the rectangle

        Return:
        int: the perimeter of the rectnangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width + self.height)*2)
