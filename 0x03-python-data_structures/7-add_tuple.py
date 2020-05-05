#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = len(tuple_a)
    y = len(tuple_b)
    tuple_z = ((tuple_a[0] if x >= 1 else 0) + (tuple_b[0] if y >= 1 else 0),
               (tuple_a[1] if x >= 2 else 0) + (tuple_b[1] if y >= 2 else 0))
    return tuple_z
