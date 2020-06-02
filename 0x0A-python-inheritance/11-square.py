#!/usr/bin/python3
"""Module for Rectangle class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represent a subclass of Rectangle
    """
    def __init__(self, size):
        """initialization"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """return a compute operation area of square"""
        return self.__size ** 2

    def __str__(self):
        """Returns string representation of this square."""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
