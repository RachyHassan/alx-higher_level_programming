#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    calc = len(sys.argv) - 1

    if calc == 0:
        print("0 arguments.")
    elif calc == 1:
        print("1 argument:")
        for c in range(calc):
            print("{}: {}".format(c + 1, sys.argv[c + 1]))
    else:
        print("{} arguments:".format(calc))
        for c in range(calc):
            print("{}: {}".format(c + 1, sys.argv[c + 1]))
