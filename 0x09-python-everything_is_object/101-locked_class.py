#!/usr/bin/python3

""" No Modules imported """


class LockedClass:
    """ prevents the user from dynamically creating
    new instance attributes
    """

    __slots__ = ["first_name"]
