#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [elt if elt != search else replace for elt in my_list]
    return new_list
