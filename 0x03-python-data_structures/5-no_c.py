#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        list_string = list(my_string)
    else:
        return None

    list_string = [char for char in list_string if char!= 'C' and char != 'c']
    list_string = ''.join(list_string)
    return list_string
