#!/usr/bin/env python3
def no_c(my_string):
    list_string = list(my_string)
    for i in list_string:
        if i == 'c' or i == 'C':
            list_string.remove(i)
    list_string = ''.join(list_string)
    return list_string
