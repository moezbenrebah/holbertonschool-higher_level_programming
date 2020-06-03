#!/usr/bin/python3
"""
Module for number_of_lines function
"""


def number_of_lines(filename=""):
    """
    Represents a function that compute and return the number of lines
    of a text file
    Arguments:
        filename: the name of text file
    Returns:
        returns the number of lines
    """
    count = 0
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            count += 1
    return count
