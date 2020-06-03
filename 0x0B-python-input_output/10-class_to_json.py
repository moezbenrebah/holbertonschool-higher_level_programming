#!/usr/bin/python3
"""
Module for serialization of an object
"""


def class_to_json(obj):
    """
    Represents:
        a function that returns the dictionary description with simple
        data structure (list, dictionary, string, integer and boolean)
        for JSON serialization of an object.
    Arguments:
        obj (object): dictionary
    Returns:
        simple data structure
    """

    return obj.__dict__
