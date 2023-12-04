#!/usr/bin/python3
"""Function that checks instance"""


def is_kind_of_class(obj, a_class):
    """Function that checks instances

    Args:
        obj (object): fetches from main
        a_class (class): fetches from main
    Returns:
        bool: is class or not
    """

    return (isinstance(obj, a_class))
