#!/usr/bin/python3
"""
Module to exchange from string to json.
"""
import json


def from_json_string(my_str):
    """
    Represents:
    a function that returns an object (Python data structure)
    represented by a JSON string.
    Argument:
        my_str (object string): string to exchange.
    Returns:
        object.
    """
    return json.loads(my_str)
