#!/usr/bin/python3
"""
This is the from_json_string module
"""
import json


def from_json_string(my_str):
    """
    This function hat returns an object (Python data structure)
    represented by a JSON string

    Parameter:
    ----------
    my_str : JSON string
    """
    return json.loads(my_str)
