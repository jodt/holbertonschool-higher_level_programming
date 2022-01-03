#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        first_a, second_a = 0, 0
    elif len(tuple_a) == 1:
        first_a = tuple_a[0]
        second_a = 0
    else:
        first_a, second_a = tuple_a
    if len(tuple_b) == 0:
        first_b, second_b = 0, 0
    elif len(tuple_b) == 1:
        first_b = tuple_b[0]
        second_b = 0
    else:
        first_b, second_b = tuple_b
    c = first_a + first_b, second_a + second_b
    return c
