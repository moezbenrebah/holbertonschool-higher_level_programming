#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        rem = ''
        if i != 'c' and i != 'C':
            print("{:s}".format(i), end="")
    return rem
