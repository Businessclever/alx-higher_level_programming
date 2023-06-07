#!/usr/bin/python3
"""
This is the "add_integer" module.
The add_integer module supplies one function, add_integer(a, b).
"""


def add_integer(a, b):
    """
    Returns the addition of two integers.

    :param a: An integer value.
    :param b: An integer value.
    :return: The sum of a and b.
    :raises TypeError: If either a or b is not an integer.
    """
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b

