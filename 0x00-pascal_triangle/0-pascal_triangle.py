#!/usr/bin/python3
"""module that defines a function to create a pascal triangle"""


def pascal_triangle(n):
    """function to create a pascal triangle"""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, len(triangle[i - 1])):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
