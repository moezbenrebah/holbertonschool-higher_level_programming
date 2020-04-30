#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    idx = len(sys.argv) - 1
    print("{} {}{}".format(idx, "argument" if idx == 1 else "arguments",
                           '.' if idx == 0 else ':'))
    for i in range(idx):
        print("{:d}: {:s}".format(i + 1, sys.argv[i + 1]))
