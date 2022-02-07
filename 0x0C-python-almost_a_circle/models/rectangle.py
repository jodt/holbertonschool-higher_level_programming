#!/usr/bin/python3
"""
This class create a rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    This class represents a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialise data

        Parameters:
        -----------
        width (int) : rectangle width
        height (int) : rectangle height
        x (int) : x
        y (int) : y
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        returns width value
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        updates width value
        """
        self.data_validator("width", width)
        self.__width = width

    @property
    def height(self):
        """
        returns height value
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        updates height value
        """
        self.data_validator("height", height)
        self.__height = height

    @property
    def x(self):
        """
        returns x value
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        updates x value
        """
        self.data_validator("x", x)
        self.__x = x

    @property
    def y(self):
        """
        returns y value
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        updates y value
        """
        self.data_validator("y", y)
        self.__y = y

    def data_validator(self, name, value):
        """
        Check type and value of arguments

        Parameters:
        -----------
        name (str) : argument name
        value : argument value

        Raises:
        -------
        TypeError :  if value is not int
        ValueError : if x or/and y is < 0
                     if width or and height <=0

        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        else:
            if (name in ["width", "height"] and value <= 0):
                raise ValueError("{} must be > 0".format(name))
            elif (name in ["x", "y"] and value < 0):
                raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """
        returns the aera of te rectangle
        """
        return self.width * self.height

    def display(self):
        """
        prints in stdout the Rectangle
        instance with the character #
        """
        for i in range(self.y):
            print("\n", end="")
        for j in range(self.height):
            for k in range(self.x):
                print(" ", end="")
            for m in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """
        returns a string with the characteristics of the rectangle
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """
        updates attributes of the rectangle
        """
        arg_list = ["id", "width", "height", "x", "y", "\0"]
        if (len(args)):
            for i in range(len(args)):
                setattr(self, arg_list[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        returns dictionnary representation of rectangle
        """
        return {
            'id': self.id, 'width': self.width,
            'height': self.height, 'x': self.x, 'y': self.y
        }
