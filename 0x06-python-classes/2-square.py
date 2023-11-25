#!/usr/bin/python3

class Square:
    """ Square class that defines geometric computation


        Attributes:
            size (int): Size of square
    """
    try:
        def __init__(self, size=0):
            """initializes the square
            Args:
                size (int): size of the square

            Returns:
                None
            """
            if size < 0:
                raise (ValueError("size must be >= 0"))
    except (TypeError):
        print("size must be an integer")
