#!/usr/bin/python3
"""
Module for student class.
"""
import json


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    """
    Represents:
        a class Student that defines a student.
    Attributes:
        first_name (string): the student first name.
        last_name (string): the student last name.
        age (integer): student age.
    Returns:
        simple data structure.
    """

    def to_json(self):
        return self.__dict__
