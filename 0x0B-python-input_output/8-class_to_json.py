#!/usr/bin/python3
"""
Module for return dict
"""


def class_to_json(obj):
    """returns dictionary representation \
            with simple data structure."""
    return obj.__dict__
