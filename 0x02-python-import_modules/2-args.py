#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    if args < 0:
            print("{} arguments".format(args))
    if args == 1:
        print("{} arguments:".format(args))
    else:
        print("{} arguments:".format(args))
    for i in range(args):
        print("{} {:s}".format(i + 1, sys.argv[i + 1]))
