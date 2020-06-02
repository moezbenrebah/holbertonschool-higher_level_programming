#!/usr/bin/python3


def lookup(obj):
    """the list of availables attributes and methods of an object"""

    """
    Arguments:
        obj: object

    Returns: list
    """
    return dir(obj)
