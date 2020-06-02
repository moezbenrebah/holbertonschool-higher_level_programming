#!/usr/bin/python3
"""Defines is_same_class() function"""


def is_same_class(obj, a_class):
    """check object is exactly an instance of the specified class
    Args:

        obj (object):
        a_class (object class):

    Returns:
        Bool
    """

    if type(obj) is a_class:
        return True
    else:
        return False
