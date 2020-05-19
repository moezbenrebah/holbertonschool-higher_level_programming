#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
                raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for x in range(self.size):
            for y in range(self.size):
                print("#", end='\n' if y is self.size - 1 and x != y else "")
        print()
