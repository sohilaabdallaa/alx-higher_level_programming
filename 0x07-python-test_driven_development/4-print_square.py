#!/usr/bin/python3
"""
No Modules Imported
"""


def print_square(size):
    """ prints a square with the character # """
    if type(size) != int:
        """ raise an error """
        raise TypeError("size must be an integer")
    if (size < 0):
        """ raise an error """
        raise ValueError("size must be >= 0")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for k in range(size):
            print('#', end="")
        print()
