#!/usr/bin/python3
"""Function thta deals with Json"""
import json


def save_to_json_file(my_obj, filename):

    """Funtion that writes an object to a text file"""

    with open(filname, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
