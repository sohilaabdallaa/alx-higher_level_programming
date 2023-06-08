#!/usr/bin/python3
if __name__ == "__main__":
    import sys
     length = len(sys.argv)
    if length == 1:
        print("{:d} {}.".format(0, "arguments"))
    elif length == 2:
        print("{:d} {}:".format(1, "argument"))
        for i in range(1, length):
            print("{:d}: {}".format(length - 1, sys.argv[i]))
    else:
        print("{:d} {}:".format(length - 1, "arguments"))
        for i in range(1, length):
            print("{:d}: {}".format(i, sys.argv[i]))
