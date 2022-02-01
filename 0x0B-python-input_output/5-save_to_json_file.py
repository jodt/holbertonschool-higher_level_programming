#!/usr/bin/python3
"""
This is the save_to_json module
"""


import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an Object to a text file,
    using a JSON representation

    Parameters:
    -----------
    my_obj :  object
    filename (str) : name file
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
