#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    answer = 0
    for a in range(len(sys.argv) - 1):
        answer += int(sys.argv[a + 1])
    print("{}".format(answer))
