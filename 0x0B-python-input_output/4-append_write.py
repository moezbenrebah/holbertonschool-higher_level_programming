#!/usr/bin/python3
"""
Module for writes strings to a text file
"""


def append_write(filename="", text=""):
    """
    Represent a function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    Arguments:
        filename (str): the name of the text file.
        text (int): the text file to write.
    Returns:
        the integers of appended strings.
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
