#!/usr/bin/python3
"""Funtion that deals with Json"""
import json


def from_json_string(my_str):
    """Funtion that returns the Python data structure
        represented by a Json string.
    """
    return json.loads(my_str)
