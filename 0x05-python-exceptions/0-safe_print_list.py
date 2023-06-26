#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    total = 0
    for i in range(x):
        total += 1
    for c in range(x):
        try:
            print("{:d}".format(my_list[c]), end="")
        except IndexError:
            pass
    print()
    return total
