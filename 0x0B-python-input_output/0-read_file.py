#!/usr/bin/python3
"""Function For file manipulation"""


def read_file(filename=""):
    """Function that reads from a file"""

    with open(filename, 'r', encoding='utf-8') as file:

        content = file.read()

        print(content, end="")
