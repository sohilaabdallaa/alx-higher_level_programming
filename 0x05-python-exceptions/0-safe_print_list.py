#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    total = 0
    for c in range(x):
        try:
            print("{:d}".format(my_list[c]), end="")
            total += 1
        except IndexError:
            pass
    print()
    return total
