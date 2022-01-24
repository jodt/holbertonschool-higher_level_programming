#!/usr/bin/python3
"""
This is the "say_my_name" module.

The say_my_name module supplies one function, say_my_name()
"""


def say_my_name(first_name, last_name=""):
    """
    Print the string : My name is <first name> <last name>
    with values of first_name and last_name

    Parameters
    ==========
    first_name (str) : the first name of the person
    last_name (str) : the last name of the person

    Raises
    ======
    TypeError : if first_name and last_name are not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
