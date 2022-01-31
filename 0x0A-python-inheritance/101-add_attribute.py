#!/usr/bin/python3

def add_attribute(obj, str1, str2):
    if obj.__class__.__module__ == "builtins":
        raise TypeError("can't add new attribute ")
    else:
        setattr(obj, str1, str2)
