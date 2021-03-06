#!/usr/bin/python3
"""
This is the load_from_json_file module
"""
import json


def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”

    Parameter:
    ----------

    """
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
