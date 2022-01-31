#!/usr/bin/python3
"""
This is the is_same_class module"
"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an
    instance of the specified class
    """
    return type(obj) == a_class
