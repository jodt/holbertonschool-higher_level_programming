#!/usr/bin/python3
"""
This is the module append_write
"""


def append_write(filename="", text=""):
    """
    This function appends a string at the end
    of a text file

    Parameters:
    -----------
    filename (str) : name file
    text (str) : text to add
    """
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
