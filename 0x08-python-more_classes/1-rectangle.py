#!/usr/bin/python3
"""Rectangle module."""


class Rectangle:
    """Defines a Rectangle.

     Attributes:
        width (int): rectangle width.
        height (int): rectangle height.
    """

    def __init__(self, width=0, height=0):
        """Initializes a rectangle
        Args:
            width (int): rectangle width.
            height (int): rectangle height.

        Raises:
            TypeError: widht and height must be an integer.
            ValueError: width and height must be >= 0.

        Returns: None
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
