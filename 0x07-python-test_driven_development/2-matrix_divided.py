#!/usr/bin/python3
"""
This is the "matrix_divided" module.

The matrix_divided module supplies one function, matrix_divided.
"""


def matrix_divided(matrix, div):
    """
    Return a new matrix with all elements divided by div

    Parameters
    ==========
    matrix : a list of lists of intergers
    div (int) : divisor value


    Raises
    ======
    TypeError : if div is not an int of a float
                if matrix is not a list of lists of integer
                if rows of the matrix have not the same size

    ZeroDivisionError: if div is equal to 0
    """

    type_ok = (float, int)
    if not isinstance(div, type_ok):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(arr, list) for arr in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for arr in matrix:
        if not all(isinstance(i, type_ok) for i in arr):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix)):
        if len(matrix[i]) != (len(matrix[0])):
            raise TypeError("Each row of the matrix must have the same size")

    return list(map(lambda arr: list((map(lambda val: round(val/div, 2), arr))), matrix))
