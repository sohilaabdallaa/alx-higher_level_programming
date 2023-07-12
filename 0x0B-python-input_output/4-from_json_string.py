#!/usr/bin/python3
"""from JSON to object module"""
import json


def from_json_string(my_str):
    """returns an object(Python data structure)
    represented by a json string"""
    return json.loads(my_str)
