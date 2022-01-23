#!/usr/bin/python3
"""
This is the "add_integer" module.

The add_integer module supplies one function, add_integer()
"""


def add_integer(a, b=98):
    """
    Return The addition of two integers a and b

    Parameters
    ==========
    a : int
    b : int

    Raise
    =====
    TypeError : if a and b are not interger or float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/0-add_integer.txt")
