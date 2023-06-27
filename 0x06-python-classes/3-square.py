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
        if type(size) != int:
            """ raise an error """
            raise TypeError("size must be an integer")
        elif (size < 0):
            """ raise an error """
            raise ValueError("size must be >= 0")
        else:
            """ initialize __size private instance variable
            """
            self. __size = size
    """ define a public instance method area
        that returns the current square area
    """
    def area(self):
        """ define a public instance method area
            that returns the current square area
        """
        return self.__size ** 2
