#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_int = {'I': 1, 'V': 5,
                 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    if (type(roman_string) is not str or roman_string is None):
        return 0
    for i, c in enumerate(roman_string):
        if ((i+1) == len(roman_string) or roman_int[c] >= roman_int[roman_string[i+1]]):
            result += roman_int[c]
        else:
            result -= roman_int[c]
    return result
