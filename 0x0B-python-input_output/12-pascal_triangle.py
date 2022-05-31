#!/usr/bin/python3
"""Pascal triangle module"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    res = []
    k = []
    for x in range(n):
        row = []
        for y in range(x + 1):
            if x == 0 or y == 0 or x == y:
                row.append(1)
            else:
                row.append(k[y] + k[y - 1])
        k = row
        res.append(row)
    return res
