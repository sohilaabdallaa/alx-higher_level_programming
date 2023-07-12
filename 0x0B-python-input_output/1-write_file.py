#!/usr/bin/python3
"""
no module imported
"""


def write_file(filename="", text=""):
    """write to text file"""
    with open(filename, encoding="utf-8", mode="w+") as f:
        return f.write(text)
