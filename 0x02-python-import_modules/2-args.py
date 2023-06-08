#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    1 = len(sys.argv)
    if l == 1:
        print("0 arguments.")
    elif l == 2:
        print("{:d} {}:".format(1, "argument"))
    else:   
        print("{:d} {}:".format(l, 1, "arguments"))
    for i in range(1, l):
        print("{:d}: {}".format(i, sys.argv[i]))

