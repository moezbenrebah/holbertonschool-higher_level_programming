#!/usr/bin/python3
"""Module for Rectangle class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represent a subclass for a rectangle class.
    """
    def __init__(self, width, height):
        """initialization"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
