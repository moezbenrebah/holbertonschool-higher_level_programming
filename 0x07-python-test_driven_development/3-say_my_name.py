#!/usr/bin/python3
"""
This is the "3-say_my_name.py" module.

The 3-say_my_name.py module function: say_my_name(first_name, last_name="").
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name: prints My names <first name> and <last name>.
    Args:
        first_name: first name string.
        last_name: last name string.

    Raises:
        TypeError: if first_name or last_name are not strings.

    Returns:
        None
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
