#!/usr/bin/python3
class Square:
    """
    This class represents a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialise Data and checks if size is and integer and not < 0"""
        self.size = size
        self.position = position

    """getter"""
    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position
    """setter"""
    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """return aera of the square"""
        return self.size ** 2

    def my_print(self):
        """print aera à the position declared"""
        if (self.size == 0):
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
