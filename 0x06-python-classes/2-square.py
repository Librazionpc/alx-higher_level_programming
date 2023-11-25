#!/usr/bin/python3
"""Module Square"""


class Square:
    """ Square class that defines geometric computation


        Attributes:
            size (int): Size of square
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of the square

        Returns:
            None
        """
        if type(size) != int:
            raise TypeError("size must be integer")
        elif size < 0:
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size
