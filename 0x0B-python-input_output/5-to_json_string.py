#!/usr/bin/python3
"""
Module for json representaion
"""
import json


def to_json_string(my_obj):
    """
    Represent a function that returns the JSON representation
    of an object (string)
    Arguments
        my_obj (object str): string to represent in json
    Returns:
        integer
    """
    return json.dumps(my_obj)
