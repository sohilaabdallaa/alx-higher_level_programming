#!/usr/bin/python3
"""
No Modules Imported
"""


def append_write(filename="", text=""):
    """append str at the end of text file"""
    with open(filename, mode="a+", encoding="utf-8") as f:
        return f.write(text)
