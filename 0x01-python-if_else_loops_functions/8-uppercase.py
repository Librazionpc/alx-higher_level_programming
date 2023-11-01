#!/usr/bin/python3
def uppercase(str):
    output = ""
    for char in str:
        if ('a' <= char <= 'z'):
            upper_char = chr(ord(char) - 32)
            output += upper_char
        else:
            output += char
    print(output)
