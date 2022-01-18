#!/usr/bin/python3
"""This module create a square"""


class Square:
    """
    This class represents a square
    """

    def __init__(self, size=0):
        """ Initialise Data and checks if size is and integer and not < 0

        Parameters:
        ----------
        size: int
            size of the square

        Raises:
        -------
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
