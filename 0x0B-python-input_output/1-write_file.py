#!/usr/bin/python3
"""Function that deals with file i/o"""


def write_file(filename="", text=""):

    """Function that writes to a file open if it doesn't
        exist and overwrite if it exist
    """
    no_chars = 0
    with open(filename, 'w+', encoding='utf-8') as file:
        file.write(text)
        file.seek(0)
        content = file.read()
        for words in content:
            for chars in words:
                no_chars += 1
    return (no_chars)
