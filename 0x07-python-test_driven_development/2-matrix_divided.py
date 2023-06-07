#!/usr/bin/python3
"""
This module defines a function for scalar division of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides a matrix by a scalar integer and rounds the result to two decimal places.

    :param matrix: A matrix (list of lists) of integers/floats.
    :param div: A number to divide the matrix by.
    :return: A new matrix with each element divided by the scalar value.
    :raises TypeError: If the matrix is not a list of lists of integers/floats,
                       if the rows of the matrix have different lengths,
                       or if the divisor is not a number.
    :raises ZeroDivisionError: If the divisor is zero.
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(error_msg)

    len_rows = []
    row_count = 0

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error_msg)
        len_rows.append(len(row))
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error_msg)
        row_count += 1

    if len(set(len_rows)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [
        [round(x / div, 2) for x in row]
        for row in matrix
    ]

    return new_matrix

