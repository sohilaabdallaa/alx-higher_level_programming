#!/usr/bin/python3
"""
No Modules Impoted
"""

def text_indentation(text):
    """
    prints a text with 2 new lines \
            after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for c in text:
        if c == '?' or c == '.' or c == ':':
            print(c)
            print()
        else:
            print(c, end="")
