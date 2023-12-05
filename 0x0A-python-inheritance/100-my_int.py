#!/usr/bin/python3
"""A Class Module"""


class Myint(int):

    """ inherit from int

    Args:
        int (int): is a rebel
    """

    def __eq__(self, other_no):
        return super().__ne__(other_no)

    def __ne__(self, other_no):
        return super().__eq__(other_no)
