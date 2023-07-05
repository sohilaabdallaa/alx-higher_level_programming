#!/usr/bin/python3
"""
No Modules Impoted
"""

def text_indentation(text):
    """
    prints a text with 2 new lines \
            after each of these characters: ., ? and :
    """
    is_special = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    for c in text:
        if is_special == 0:
            if c == '':
                continue
            else:
                is_special = 1

        if is_special == 1:
            if c == '?' or c == '.' or c == ':':
                print(c)
                print()
                is_special = 0
            else:
                print(c, end="")
