#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    if num == 1:
        print("0 arguments.")
    elif num == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(num - 1))
    for i in range(num - 1):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
