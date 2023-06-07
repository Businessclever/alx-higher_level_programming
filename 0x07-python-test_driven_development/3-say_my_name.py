#!/usr/bin/python3
"""
This is the "say_my_name" module.
The say_my_name module supplies one function, say_my_name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is" followed by the first name and optional last name.

    :param first_name: A string representing the first name.
    :param last_name: An optional string representing the last name.
    :raises TypeError: If the first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is", first_name, last_name)

