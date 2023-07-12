#!/usr/bin/python3
"""
0-read_file module to read from text file
"""


def read_file(filename=""):
    """
    read text file and print it to stdout
    """
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
