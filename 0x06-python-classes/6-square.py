#!/usr/bin/python3
"""
No Modules imported
"""


class Square:
    """
    define a function called __init__
    to initialize size and position tuple
    """
    def __init__(self, size=0, position=(0, 0)):
        """initialize __size private instance variable
            __position is tuple of the 2D Square
        """
        self.size = size
        self.position = position

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
            self.__size = value
    """ define a public instance method area
        that returns the current square area
    """
    def area(self):
        """ define a public instance method area
            that returns the current square area
        """
        return self.__size ** 2

    @property
    def position(self):
        """ getter function for retrive the position att
            return the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ setter function for set the tuple position
            no return """
        """ if statment """
        if not (isinstance(value, tuple) and len(value) == 2 and
                isinstance(value[0], int) and value[0] >= 0 and
                isinstance(value[1], int) and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """ that prints in stdout the square with the character """
        if (self.size == 0):
            print()
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            for k in range(self.position[0]):
                print(" ", end="")
            for k in range(self.size):
                print('#', end="")
            print()
