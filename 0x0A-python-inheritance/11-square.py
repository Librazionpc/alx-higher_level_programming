#!/usr/bin/python3
"""Square Module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialize Square"""
        super().__init__(size, size)
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size <= 0):
            raise ValueError("size must be greater than 0")
        self.__size = size

    def __str__(self):
        """String representation"""
        return "[Square] {}/{}".format(self.__size, self.__size)
