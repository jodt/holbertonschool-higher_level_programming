#!/usr/bin/python3
"""
This is read_fiel module
"""


def read_file(filename=""):
    """
    This function read and print on stdout a text file

    Parameter
    ---------
    filename (str) : name of the file
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
