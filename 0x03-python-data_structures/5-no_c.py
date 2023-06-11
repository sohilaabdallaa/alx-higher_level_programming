#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        list_string = list(my_string)
    else:
        return None
    for i in list_string:
        if i == 'c' or i == 'C':
            list_string.remove(i)
    list_string = ''.join(list_string)
    return list_string
