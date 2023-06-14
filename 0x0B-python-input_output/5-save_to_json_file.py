#!/usr/bin/python3
"""
Defines a JSON file-writing function.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using JSON representation.

    Args:
        my_obj: The object to write to the file.
        filename: The name of the file to write.

    Returns:
        None.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)

