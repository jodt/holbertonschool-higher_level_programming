#!/usr/bin/python3
"""
This is the to_json_string module
"""
import json


def to_json_string(my_obj):
    """
    This function that returns the JSON
    representation of an object

    Parameter:
    ---------
    my_obj : object
    """
    return json.dumps(my_obj)
