#!/usr/bin/python3
def best_score(a_dictionary):
    new_list = dict()
    if a_dictionary:
        for k, v in a_dictionary.items():
            if a_dictionary[k] is not None:
                new_list[k] = v
        if len(new_list) == 0:
            return None
        else:
            return max(list(new_list.values()))
