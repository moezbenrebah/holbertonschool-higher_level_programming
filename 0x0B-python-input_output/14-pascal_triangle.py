#!/usr/bin/python3
"""Module for pascal triangle function"""


def pascal_triangle(n):
    """
    Represents:
         function that returns a list of lists of integers
         representing the Pascal’s triangle.
    Argument:
         n (integer): integer will be fill in list.
    Returns:
         list.
    """
    if n <= 0:
        return []
    else:
        list = [[] for i in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if(j < i):
                    if(j == 0):
                        list[i].append(1)
                    else:
                        list[i].append(list[i - 1][j] + list[i - 1][j - 1])
                elif(j == i):
                    list[i].append(1)
        return list
