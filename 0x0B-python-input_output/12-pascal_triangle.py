#!/usr/bin/python3
"""
This is the pascal_triangle module
"""


def pascal_triangle(n):
    """
    This funtcion returns list of n lists
    wich represents pascal_triangle
    """
    my_list = [[] for i in range(n)]
    for i in range(n):
        for j in range(i+1):
            if (j < i):
                if (j == 0):
                    my_list[i].append(1)
                else:
                    my_list[i].append(my_list[i-1][j] + my_list[i-1][j-1])
            elif(j == i):
                my_list[i].append(1)
    return my_list
