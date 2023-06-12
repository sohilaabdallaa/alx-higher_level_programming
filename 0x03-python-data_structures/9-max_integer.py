#!/usr/bin/python3
def max_integer(my_list=[]):
    maxi = my_list[0]
    if not my_list:
        return None
    for i in range(1, len(my_list)):
        if isinstance(my_list[i], int):
            if my_list[i] >= maxi:
                maxi = my_list[i]
    return maxi
