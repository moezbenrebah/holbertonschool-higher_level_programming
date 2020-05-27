#!/usr/bin/python3
"""
This is the "2-matrix_divided.py" module.

The 2-matrix_divided.py module function: def matrix_ div).
"""


def matrix_divided(matrix, div):
    """
    matrix_divided: divides all elements of a matrix
    Args:
        matrix (int, float):  list of lists of integers or floats
        div (int): divident
    Returns:
        int
    Raises:
        TypeError: If matrix is not list of lists containing int or float.
        TypeError: If sublists are not all same size.
        TypeError: If div is not int or float.
        ZeroDivisionError: If div is zero.
    """

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        if not isinstance(i, list) or len(i) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(j / div, 2) for j in i] for i in matrix]
