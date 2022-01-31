#!/usr/bin/python3
"""
This is the base_geometry module
"""


class BaseGeometry:
    """This is a class BaseGeometry"""

    def area(self):
        """
        raise exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This function validates value

        Parameters:
        -----------
        name (str) : name
        value (int) : value

        Raises:
        -------
        TypeError: if value is not an int
        ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
