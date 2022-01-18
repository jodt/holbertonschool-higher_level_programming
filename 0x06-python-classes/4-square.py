#!/usr/bin/python3
"""This module create a square"""


class Square:
    """
    This class represents a square"""

    def __init__(self, size=0):
        """ Initialise Data

        Parameters
        ----------
        size : int
            size of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        getter to access of the size value

        Return
        ------
        int
            size value
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        setter to update size value

        Parameter
        ---------
        size: int
            size of the square

        Raises
        ------
        Typerror
            If size is not an integer
        ValueError
            If size is > 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculate the aera of the square

        Returns
        -------
        int
            the aera of the square
        """
        return self.size ** 2
