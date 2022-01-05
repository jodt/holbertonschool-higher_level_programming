#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key = []
    for k, v in a_dictionary.items():
        if value in a_dictionary.values():
            if v == value:
                key.append(k)
                for ky in key:
                    del(a_dictionary[ky])
            return a_dictionary
