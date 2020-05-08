#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return list(set(set_1).symmetric_difference(set(set_2)))
