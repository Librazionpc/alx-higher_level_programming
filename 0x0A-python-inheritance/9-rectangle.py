#!/usr/bin/python3
"""Rectangle Module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize Rectangle"""
        if (type(width) != int):
            raise TypeError("width {} must be an integer")
        if (width < 0):
            raise ValueError("width must be greater than 0")
        if (type(height) != int):
            raise TypeError("height {} must be an integer")
        if (height < 0):
            raise ValueError("height must be greater than 0")
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate area"""
        return self.__width * self.__height

    def __str__(self):
        """String representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
