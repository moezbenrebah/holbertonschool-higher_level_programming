#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
         """Constructor.
        Args:
            size: Length of a side of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Property for the length of a side of this square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
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
        """Prints this square."""
        for x in range(self.size):
            for y in range(self.size):
                print("#", end='\n' if y is self.size - 1 and x != y else "")
        print()
