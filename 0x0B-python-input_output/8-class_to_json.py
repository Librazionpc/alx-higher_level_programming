#!/usr/bin/python3
"""Function that get description of object Json"""


def class_to_json(obj):

    """function that returns the dictionary description with simple
        data structure (list, dictionary, string, integer and boolean)
        for JSON serialization of an object:
    """
    new_dict = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, bool, str, int)):
            new_dict[key] = value
    return (new_dict)
