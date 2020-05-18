#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        if int(value):
            return True
    except ValueError:
        return False
    return value
