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

    def area(self):
        """
        set square area

        Return:
            The current area (int)
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        getter of size

        Return:
            Size of square gotten
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Setter of size

        Args:
            size (int): size of the square
        Raises
            TypeError: if size is not int
            ValueError: size less than 0
        Returns:
            None
        """
        if (type(value) != int):
            raise (TypeError("size must be an integer"))
        elif (value < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = value
