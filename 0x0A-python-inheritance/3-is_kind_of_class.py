#!/usr/bin/python3
"""
This is the is_kin_of_class module
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class
    """
    return isinstance(obj, a_class)
