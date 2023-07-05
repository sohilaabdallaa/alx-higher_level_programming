#!/usr/bin/python3
""" No Modules Imported """


def matrix_divided(matrix, div):
    """ function that divides all elements of a matrix. """

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    newMat = []
    rows = []
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if type(row) is not list:
            raise TypeError(
                    "matrix must be a matrix (list of lists) \
                            of integers/floats")
        for colNum in row:
            if not isinstance(colNum, (int, float)):
                raise TypeError(
                        "matrix must be a matrix (list of lists) of \
                                integers/floats")
            rows.append(round(colNum/div, 2))
        newMat.append(rows)
        rows = []
    return newMat
