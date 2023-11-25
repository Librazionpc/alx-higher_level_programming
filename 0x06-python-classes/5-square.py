#!/usr/bin/python3

class Sqaure:
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

    @size.setter
    def size(self, value):
        """
        set square area

        Return:
            The current area (int)
        """
        if (type(value) != int):
            raise (TypeError("size must be >= 0"))
        elif value < 0:
            raise (ValueError("size must be an integer"))
        else:
            self.__size = value

    @property
    def size(self):
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
        return (self.value)

    def area(self):
        """
        set square area

        Return:
            the current square area (int)
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        print a sqaure from the size using ##

        Returns:
            None
        """
        if (self.__size == 0):
            print()
        for i in range(0, self.__size):
            for i in range(0, self.__size):
                print("#".end="")
            print()
