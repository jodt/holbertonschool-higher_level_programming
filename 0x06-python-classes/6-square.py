#!/usr/bin/python3
"""This module create a square"""


class Square:
    """
    This class represents a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialise Data

        Parameters
        ----------
        size : int
            size of the square
        position: tuple
            position of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        getter to access of values of the postion

        Return
        ------
        tuple
            values of the position
        """
        return self.__position

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
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @position.setter
    def position(self, value):
        """
         setter to update values of position

        Parameter
        ---------
        value: tuple
            values of the postion of the square

        Raises
        ------
        Typerror
            If value is not a tuple or if elements of the tuple
            are not integer or if elements of the tuple are < 0
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        calculate the aera of the square

        Returns
        -------
        int
            the aera of the square
        """
        return self.size ** 2

    def my_print(self):
        """print aera à the position declared"""
        if self.size == 0:
            print()
        else:
            for j in range(self.position[1]):
                print()
            for k in range(self.size):
                for m in range(self.position[0]):
                    print("{}".format(" "), end="")
                for n in range(self.size):
                    print("{}".format("#"), end="")
                print()
