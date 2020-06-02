#!/usr/bin/python3
"""Defines inherits_form() function"""


def inherits_from(obj, a_class):
    """
    checks if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class

    Arguments:
        obj: object
        a_class: class object

    Returns:
        Bool
    """

    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
