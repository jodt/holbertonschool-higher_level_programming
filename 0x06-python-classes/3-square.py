#!/usr/bin/python3
class Square:
    """
    This class represents a square
    """

    def __init__(self, size=0):
        """ Initialise Data and checks if size is and integer and not < 0"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """return aera of the square"""
        return self.__size ** 2
