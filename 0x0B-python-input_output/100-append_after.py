#!/usr/bin/python3
"""Module for appending line of text to a file."""


def append_after(filename="", search_string="", new_string=""):
    """
    Represent:
        a function that inserts a line of text to a file,
        after each line containing a specific string.
    Arguments:
        filename (string): the file name.
        search_string (string): reference string.
        new_string (string): new string to insert.
    Returns:
        None.
    """
    with open(filename, 'r+', encoding="utf-8") as f:
        word = ""
        for lines in f:
            word += lines
            if search_string in lines:
                word += new_string
        f.seek(0)
        f.write(word)
