#!/usr/bin/python3
"""
This is the "text_indentation" module

The text_indentation module supplies one function, text_indetation()
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Parameter
    =========
    text (string) : a text

    Raise
    ======
    TypeError: if text is not a string
    """
    is_char = [".", "?", ":", " "]
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if text.isspace():
        return
    text = text.strip()
    for i in range(len(text)):
        if text[i] in [".", "?", ":"]:
            print("{}".format(text[i]), end="")
            print()
            print()
        elif (i - 1) != -1 and text[i] == " " and text[i-1] in is_char:
            continue
        else:
            print("{}".format(text[i]), end="")
