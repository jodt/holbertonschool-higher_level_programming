#!/usr/bin/python3
"""
This is the peak module
"""


def find_peak(list_of_integers):
    """
    this function finds a peak in a list of unsorted integers
    """
    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    elif abs(list_of_integers[0]) > abs(list_of_integers[1]):
        return list_of_integers[0]
    elif (abs(list_of_integers[-1] >= list_of_integers[-2])):
        return list_of_integers[-1]
    else:
        for i in range(1, len(list_of_integers) - 1):
            if (abs(list_of_integers[i] - 1) <=
                    abs(list_of_integers[i]) >= abs(list_of_integers[i + 1])):
                return list_of_integers[i]
