#!/usr/bin/python3
"""
    No Module imported
"""


class Student:
    """Defines student class"""
    def __init__(self, first_name, last_name, age):
        """
            Instantiation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            retrieves a dictionary representation of Student instance
        """
        if type(attrs) == list and all(type(elem) == str for elem in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
