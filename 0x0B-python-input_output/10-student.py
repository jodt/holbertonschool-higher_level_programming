#!/usr/bin/python3
"""
This module creates
"""


class Student:
    """
    This class represents student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialise data

        Parameters:
        -----------
        first_name (str): student firest name
        last_name (str) : student last name
        age (int) : student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionnary of instance object

        Parameters
        ----------
        attrs : list of key to display
        """
        if type(attrs) is list:
            for elt in attrs:
                if type(elt) is str:
                    d = {k: v for k, v in self.__dict__.items() if k in attrs}
                    return d
                else:
                    return self.__dict__
        else:
            return self.__dict__
