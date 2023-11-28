#!/usr/bin/python3
"""Module Rectangle"""


class Rectangle:
    """
    Function that create a Rectangle Class
    Attributes:
    width (int): Width of rectangle
    height (int): Height if rectangle
    """
    def __init__(self, width=0, height=0):
        """
            initializes the public attributes

            width (int): Width of the rectangle
            height (int): Height of the rectangle

            Return: Nothing
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
            Retrives width

            Return: self.__width (The width of the retangle)
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
            Sets the width

            Attrinbutes:
                value (int): The value of the width needed

            Returns: Nothing
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            Retrives width

            Return: self.__width (The width of the retangle)
        """
        return (self.__height)

    @width.setter
    def height(self, value):
        """
            Sets the width

            Attributes:
                value (int): The value of the width needed

            Returns: Nothing
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """
            Calculate the area of the rectangle

            Uses Class attributes

            Return: The area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
            Calculate the perimeter of the rectangle

            Uses Class attributes

            Return: The perimeter of the rectangle if height
                or width not equal to zero else return zero
        """
        if (self.__height == 0 or self.__width == 0):
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """print the # according to the parameter given

        Returns:
            _type_: string
        """
        if (self.__height == 0 or self.__width == 0):
            return ("")
        rectangle = ""

        for i in range(0, self.__height):
            rectangle += "#" * self.__width
            if i < self.__height:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        """Gets the reprentation of the string

        Returns:
            string: The string passed
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Delete instamces when needed
        """
        print("Bye rectangle...")
