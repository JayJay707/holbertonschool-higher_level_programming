#!/usr/bin/python3
"""Module to divide all elements in a matrix"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix"""
    new = []

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if div is None or type(div) is not int or type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        for j in range(len(matrix[i])):
            if type(matrix[i][j]) is not int or type(matrix[i][j]) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if len(matrix[i]) != len(matrix[0]):
                raise TypeError("Each row of the matrix must have the same size")
            new.append(round((matrix[i][j]) / div, 2))
    return new
