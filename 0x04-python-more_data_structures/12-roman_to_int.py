#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    d_1 = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100,
           "XC": 90, "L": 50, "XL": 40, "X": 10, "V": 5, "IV": 4, "I": 1}
    res = 0
    prev = 0
    for i in roman_string:
        if d_1[i] > prev:
            res += d_1[i] - 2 * prev
        else:
            res = d_1[i]
    return res
