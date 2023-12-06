#!/usr/bin/python3
"""Function that deals file i/o"""


def append_write(filename="", text=""):

    """function that appends a string at the end of a
        text file (UTF8) and returns the number of characters added
    """
    no_chars = 0
    with open(filename, 'a+', encoding='utf-8') as file:
        file.write(text)

        file.seek(0)
        content = file.read()
        for words in content:
            for chars in words:
                no_chars += 1
    return (no_chars)
