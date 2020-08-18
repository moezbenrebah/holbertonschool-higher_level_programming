#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""

    i = 0
    p = list_of_integers

    if type(p) is not list:
        return None
    if len(p) is 1:
        return p[0]
    if len(p) == 0:
        return None
    for i in range(len(p) - 1):
        if p[i] >= p[i - 1] and p[i] >= p[i + 1]:
            return p[i]
        if p[i - 1] > p[i - 2] and p[i - 1] > p[i]:
            return p[i - 1]
