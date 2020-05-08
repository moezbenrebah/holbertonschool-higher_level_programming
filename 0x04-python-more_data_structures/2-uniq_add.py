#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for unique in set(my_list):
        sum += unique
    return sum
