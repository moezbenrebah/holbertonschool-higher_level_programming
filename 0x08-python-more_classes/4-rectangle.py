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
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        get rectangle width

        Returns:
            Private instance attribute __width
        """
        return self.__width

    @property
    def height(self):
        """
        get rectangle height

        Returns:
            Private instance attribute __height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        set of rectangle width
        Args:
            value (int): the width value of the rectangle
        Returns:
            None
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        set of rectangle height
        Args:
            value (int): the height value of the rectangle
        Returns:
            None
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        calculate the width of Rectangle.
        Returns:
            the width.
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        calculate the perimeter of Rectangle.
        Returns:
            the perimeter.
        """

        if self.__width == 0:
            return 0
        elif self.__height == 0:
            return 0
        else:
            return 2 * self.__width + 2 * self.__height

    def __str__(self):
        r = []
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            [r.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                r.append('\n')
        return ("".join(r))

    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.width, self.height)
