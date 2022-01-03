#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for letter in my_string:
        if (letter == "C" or letter == "c"):
            continue
        new_string += letter
    return new_string
