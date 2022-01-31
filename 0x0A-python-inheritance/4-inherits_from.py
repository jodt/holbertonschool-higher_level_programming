#!/usr/bin/python3
"""
This is the inherits_from module
"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class"""
    if (type(obj)) is not a_class:
        return (issubclass(type(obj), a_class))
