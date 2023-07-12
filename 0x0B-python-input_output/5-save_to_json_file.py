#!/usr/bin/python3
"""writes using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a\
            text file, using a json representation"""
    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
