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
        """initialize __size private instance variable
        """
        try:
            self. __size = size
            if (size < 0):
                raise ValueError("size must be >= 0")
            elif type(size) != int:
                raise TypeError("size must be an integer")
