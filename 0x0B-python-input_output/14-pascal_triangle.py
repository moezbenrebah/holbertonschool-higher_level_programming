#!/usr/bin/python3

def pascal_triangle(n):
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
