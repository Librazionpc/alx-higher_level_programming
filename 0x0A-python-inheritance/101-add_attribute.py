#!/usr/bin/python3
"""Fuction that deals with attribute"""


def add_attribute(obj, attribute, value):
    """the function"""
    if (hasattr(obj, "__dict__")):
        setattr(obj, attribute, value)
    else:
        raise TypeError("Can't add new attribute")
