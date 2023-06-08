#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 atguments.")
    elif len(sys.argv) == 2:
        print("{:d} {}:".format(1, "argument"))
    else:   
        print("{:d} {}:".format(len(sys.argv) - 1, "arguments"))
    length = len(sys.argv)
    for i in range(1, length):
        print("{:d}: {}".format(i, sys.argv[i]))

