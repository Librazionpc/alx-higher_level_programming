#!/usr/bin/python3
"""My Function that intances"""

def is_same_class(obj, a_class):
    """Checks intances

    Args:
        obj (object): gotten from main.py
        a_class (class): gotten from main.py

    Returns:
        bool: if is class
    """
    if ((isinstance(obj, a_class)) == 0):
        return (True)
    return (False)
