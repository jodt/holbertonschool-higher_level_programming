#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = [list(map(lambda x: x * x, arr)) for arr in matrix]
    return (new_list)
