#!/usr/bin/python3
"""Defines is_kind_of_class() function"""


def is_kind_of_class(obj, a_class):
    """
    checks if the object is an instance

    Arguments:
        object: obj
        object class: object class

    Returns:
        Bool
    """

    if type(obj) is a_class:
        return True
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
