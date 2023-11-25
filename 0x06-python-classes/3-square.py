#!/usr/bin/python3

class Square:
    """ Square class defined by geometric shap

        Attributes:
            size (int): Size of the square
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of the square

        Returns:
            None
        """

        self.__size = size
        if (type(size) != int):
            print("size must be an integer")
        if (size < 0):
            raise (ValueError("size must be >= 0"))

    def area(self):
        """
        set square area

        Return:
            The current area (int)
        """
        return (self.__size ** 2)
