#!/usr/bin/python3
"""
This is add_attribute module
"""


def add_attribute(obj, str1, str2):
    """
    Add a new attribute in an object if possible

    Parameters:
    -----------
    obj : object
    str1 : name of the attribute
    str2 : value of the attribute

    Raise:
    ------
    TypeError: if it's not possible to add new attribute
    """
    if (hasattr(obj, "__dict__")):
        setattr(obj, str1, str2)
    else:
        raise TypeError("can't add new attribute")
