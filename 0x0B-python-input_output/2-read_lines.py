#!/usr/bin/python3
"""
Module for read lines from a file text
"""


def read_lines(filename="", nb_lines=0):
    """
    Represent a function that number of lines from a text file
    Argument:
        filename: the name of text file
        nb_lines: the number of lines to be read
    Return:
        None
    """
    with open(filename, 'r', encoding="utf-8") as file:
        if nb_lines <= 0:
            print(file.read(), end="")
        for lines in file:
            print(lines, end="")
            nb_lines -= 1
            if nb_lines <= 0:
                break
