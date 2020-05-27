#!/usr/bin/python3
"""
This is the "4-print_square.py" module.

The 4-print_square.py module function: def print_square(size).
"""


def print_square(size):
    """Method for printing a square with # characters.
    Args:
        size: The int size of the square's side.
    Raises:
        TypeError: If size is not an int.
        ValueError: If size is < 0.
        TypeError: if size is < 0 and size is a float.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
