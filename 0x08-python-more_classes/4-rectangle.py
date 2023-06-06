#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Representation of a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self._width = width
        self._height = height

    @property
    def width(self):
        """Getter for the private instance attribute width"""
        return self._width

    @width.setter
    def width(self, value):
        """Setter for the private instance attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Getter for the private instance attribute height"""
        return self._height

    @height.setter
    def height(self, value):
        """Setter for the private instance attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self._width * self._height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self._width == 0 or self._height == 0:
            return 0
        return (self._width * 2) + (self._height * 2)

    def __str__(self):
        """Returns a printable string representation of the rectangle"""
        string = ""
        if self._width != 0 and self._height != 0:
            string += "\n".join("#" * self._width for _ in range(self._height))
        return string

    def __repr__(self):
        """Returns a string representation of the rectangle for reproduction"""
        return f"Rectangle({self._width}, {self._height})"

