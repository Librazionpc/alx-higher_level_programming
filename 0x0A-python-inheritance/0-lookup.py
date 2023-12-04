#!/usr/bin/python3
"""My lookup obj"""

def lookup(obj):
    """a look up object

    Args:
        obj (object): get object from main

    Returns:
        attributes and methods: of an object
    """
    return dir(obj)
