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
        self. __size = size

    @property
    def size(self):
        """ this works as getter to retrieve private
            instance attribute called size.
            it like making size private attribute public.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ it is a setter method to set the private
            attribute size with value
        """
        """ if statment """
        if type(value) != int:
            """ raise an error """
            raise TypeError("size must be an integer")
        elif (value < 0):
            """ raise an error """
            raise ValueError("size must be >= 0")
        else:
            """ initialize __size private instance variable
            """
            self. __size = value
    """ define a public instance method area
        that returns the current square area
    """
    def area(self):
        """ define a public instance method area
            that returns the current square area
        """
        return self.__size ** 2
