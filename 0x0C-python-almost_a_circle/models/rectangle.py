#!/usr/bin/python3
"""class Rectangle inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """
    Class Implementation
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class Constractor
        Args:
        __width -> width
        __height -> height
        __x -> x
        __y -> y
        super() function that will make the child class\
                inherit all the methods and properties from its parent
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def width(self):
        """
        getter to retrieve the private instance attribute width
        """
        return self.__width


    @width.setter
    def width(self, value):
        """
        width setter
        """
        if type(value) != int:
            """ raise an error """
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value


    @property
    def height(self):
        """ getter for height """
        return self.__height


    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) != int:
            """ raise an error """
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value


    @property
    def x(self):
        """x getter"""
        return self.__x


    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) != int:
            """ raise an error """
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value


    @property
    def y(self):
        """y getter"""
        return self.__y


    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) != int:
            """ raise an error """
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    def area(self):
        """ Function to calculate area of rectangle """
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance with the character # """
        for x in range(self.__height):
            for y in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """represents the class objects as a string"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
