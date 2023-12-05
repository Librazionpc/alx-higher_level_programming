#!/usr/bin/python3
"""MyInt Module"""


class MyInt(int):
    """MyInt class inheriting from int"""

    def __init__(self, num):
        """Initialize MyInt with an integer"""
        self.num = num

    def __eq__(self, other):
        """Override the == operator"""
        return self.num != other

    def __ne__(self, other):
        """Override the != operator"""
        return self.num == other
