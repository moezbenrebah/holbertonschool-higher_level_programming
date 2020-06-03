#!/usr/bin/python3
"""
Module to read a text file
"""


def read_file(filename=""):
    """
    Represent a function that reads a text and print it
    Arguments:
        filename: the name of text file to read.
    Return:
        None.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
