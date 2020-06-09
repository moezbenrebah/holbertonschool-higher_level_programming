#!/usr/bin/python3
"""Module for square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square class."""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns an update about the square"""
        return "[{}] ({}) {}/{} - {}".\
            format(type(self).__name__, self.id, self.x, self.y,
                   self.size)

    @property
    def size(self):
        """get the x coordinate of the Rectangle."""
        return self.__size

    @size.setter
    def size(self, value):
        """set the x coordinate of the Rectangle."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def update(self, *args, **kwargs):
        """update list of arguments."""
        if len(args) > 1:
            for a, arg in enumerate(args):
                if a == 0:
                    self.id = arg
                if a == 1:
                    self.size = arg
                if a == 2:
                    self.x = arg
                if a == 3:
                    self.y = arg

        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """update square attributes
        Args:
            None
        Returns:
            the dictionary representation of a square.
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
