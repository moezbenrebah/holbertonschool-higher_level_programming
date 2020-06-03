#!/usr/bin/python3
"""
Module for creating object from a "json file"
"""
import json


def load_from_json_file(filename):
    """
    Represents:
        a function that creates an Object from a “JSON file”.
    Arguments:
        filename (str): the file name.
    Returns
        object.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(filename)
