#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv)
    if l == 1:
        print("{:d} arguments.".format(0))
    elif l == 2:
        print("{:d} argument:".format(1))
    else:
        print("{:d} arguments".format(l - 1))

    for i in range(1, l):
        print("{:d}: {}".format(i, sys.argv[i]))

