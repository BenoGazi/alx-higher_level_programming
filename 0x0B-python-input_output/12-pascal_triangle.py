#!/usr/bin/python3
"""Defines a Pascals Triangle"""
def pascal_triangle(n):
    """Represent Pascal Triangle of n size.
    Returns a list of integers representing the
    Pascal's Triangle"""
    if n <= 0:
        return []
    triangles = [[1]]
    while len(triangles) < n:
        l_row = triangles[-1]
        temp = [1]
        for t in range(1, len(l_row)):
            temp.append(l_row[t - 1] + l_row[t])
        temp.append(1)
        triangles.append(temp)
    return triangles
