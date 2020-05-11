#!/usr/bin/python3
def weight_average(my_list=[]):
    if not len(my_list):
        return 0
    average = 0
    size = 0
    for a in my_list:
        average += (a[0] * a[1])
        size += a[1]
    return (average / size)
