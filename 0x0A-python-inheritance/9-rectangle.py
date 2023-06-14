#!/usr/bin/python3
"""
Defines a class Rectangle that inherits from BaseGeometry.
"""
from typing import Union


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not yet implemented."""
        raise NotImplementedError("area() is not implemented")

    @staticmethod
    def integer_validator(name: str, value: int):
        """Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width: int, height: int):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self) -> int:
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self) -> str:
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + self.__class__.__name__ + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string

