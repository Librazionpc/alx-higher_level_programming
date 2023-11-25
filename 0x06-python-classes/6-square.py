#!/usr/bin/python3
"""Module Square"""


class Square:
    """ Square class defined by geometric shap

        Attributes:
            size (int): Size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes the square
        Args:
            size (int): size of the square

        Returns:
            None
        """
        self.__size = size
        self.__position = position

    def area(self):
        """
        set square area

        Return:
            the current square area (int)
        """
        return (self.__size ** 2)

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
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        set square area

        Return:
            The current area (int)
        """

        if (type(value) != int):
            raise (TypeError("size must be an integer"))
        elif (value < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = value

    @property
    def position(self):
        """
        get postion attribute
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
            setter of position
        Args:
            value (tuple): position of the square in 2D space
        Returns:
            None
        """

        if (type(value) != tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) != int or type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print('\n'*self_position[1], end='')
            for i in range(0, self.__size):
                print(''* self.__position[0] + "#" * self.__size)
