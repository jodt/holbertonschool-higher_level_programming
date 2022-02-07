#!/usr/bin/python3
"""
This class create a square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class represents a square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialise Data
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        return size value
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        update size value
        """
        self.data_validator("width", size)
        self.__size = size

    def __str__(self):
        """
        returns a string with the characteristics of the square
        """
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """
        updates attributs of the square
        """
        arg_list = ["id", "size", "x", "y", "\0"]
        if (len(args)):
            for i in range(len(args)):
                setattr(self, arg_list[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        returns dictionnary representation of square
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
