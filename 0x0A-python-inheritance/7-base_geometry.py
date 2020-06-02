#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """
    BaseGeometry class
    """

    def area(self):
        """Methode to calculate area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
