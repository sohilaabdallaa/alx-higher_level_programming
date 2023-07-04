#!/usr/bin/python3
""" No Modules Imported """


class Rectangle:
    """ Rectangle Class """
    def __init__(self, width=0, height=0):
        """ Instantiation of width & heigth """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self__.height = height

    @property
    def width(self):
        """ width getter to return width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter to set value
            for private attribute width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ heigth getter to return heigth value """
        return self.__height

    @height.setter
    def height(self, value):
        """ heigth setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
