#!/usr/bin/python3
"""
Module for writes strings to a text file
"""


def write_file(filename="", text=""):
    """
    Represent a function that writes strings and returns the number
    of strings.
    Arguments:
        filename (str): the name of the text file.
        text (int): the text file to write.
    Returns:
        the integers of written strings.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
