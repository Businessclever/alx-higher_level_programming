#!/usr/bin/python3
"""
Defines a JSON file-reading function.
"""
import json


def load_from_json_file(filename):
    """
    Create a Python object from a JSON file.

    Args:
        filename: The name of the JSON file to read.

    Returns:
        The Python object created from the JSON file.
    """
    with open(filename) as file:
        return json.load(file)

