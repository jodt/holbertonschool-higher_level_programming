#!usr/bin/python3
"""
This is the "print_square" module.

The print_square module supplies one function, print_square()
"""


def print_square(size):
    """
    Prints a square of the size value

    Parameter
    =========
    size (int) : size length of the square

    Raises
    ======
    TypeError : if size is not an integer
    ValueError: if size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("{}".format("#"), end=(""))
        print()
