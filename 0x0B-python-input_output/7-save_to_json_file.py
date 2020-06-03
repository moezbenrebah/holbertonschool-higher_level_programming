#!/usr/bin/python3
"""
Module for write and save in json.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Represents:
        a function that writes an Object to a text file,
        using a JSON representation.
    Arguments:
        my_obj (object str): string to exchange.
        filename (str): the file name.
    Returns:
        None.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
