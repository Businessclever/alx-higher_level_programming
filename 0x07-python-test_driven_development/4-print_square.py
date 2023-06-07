#!/usr/bin/python3
"""
This is the "print_square" module.
The print_square module supplies one function, print_square(size).
"""


def print_square(size):
    """
    Prints a square with '#'s that has a side length of size.

    :param size: An integer representing the side length of the square.
    :raises TypeError: If the size is not an integer.
    :raises ValueError: If the size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")

