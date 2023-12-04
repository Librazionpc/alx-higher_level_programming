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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
