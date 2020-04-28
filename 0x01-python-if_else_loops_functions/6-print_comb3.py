#!/usr/bin/python3
for a in range(9):
    for b in range(a, 10):
        if a < b:
            print("{:d}{:d}".format(a, b),
                  end="\n" if a is 8 and b is 9 else ", ")
