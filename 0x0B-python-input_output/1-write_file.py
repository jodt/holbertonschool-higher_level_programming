#!/usr/bin/python3
"""
This is the write_file module
"""


def write_file(filename="", text=""):
    """
    This functions write create the txt file if doesn't exist
    and write inside

    Parameters:
    -----------
    filename (str) : name file
    text (str) : text to add
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
