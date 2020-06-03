#!/usr/bin/python3
"""Module for Studen class"""


class Student:
    """Class for student"""
    def __init__(self, first_name, last_name, age):
        """Constructor."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dictionary"""
        return self.__dict__.copy()
