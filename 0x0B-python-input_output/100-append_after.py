#!/usr/bin/python3
"""
This is the append_after module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This function inserts a new string in a file if the previous
    string contain a specific word

    Parameters:
    -----------
    filename(str) : file name
    search_string (str) : word that previous string must contain
    new_string (str) : string to insert
    """
    with open(filename, "r", encoding="utf-8") as f:
        contents = f.readlines()

    result = []

    for i in range(len(contents)):
        result.append(contents[i])
        if search_string in contents[i]:
            result.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.write("".join(result))
