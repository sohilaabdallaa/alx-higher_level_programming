#!/usr/bin/python3
"""
No Modules imported
"""


class Square:
    """
    define a function called __init__
    to initialize size
    """
    def __init__(self, size=0):
        """ if statment """
        if (size < 0):
            """ raise an error """
            raise ValueError("size must be >= 0")
        elif type(size) != int:
            """ raise an error """
            raise TypeError("size must be an integer")
        else:
            """ initialize __size private instance variable
            """
            self. __size = size
