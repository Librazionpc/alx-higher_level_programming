#!/usr/bin/python3
""" A Class module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle validation

    Args:
        BaseGeometry (class): integer validaition
    """
    def __init__(self, width, height):
        """intitializing rectangle"""
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
