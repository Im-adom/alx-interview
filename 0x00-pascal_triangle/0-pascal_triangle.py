#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def pascal_triangle(n):
    """returns a list of lists of numbers
    representing the pascal triangle"""
    if n <= 0:
        return []

    pascal_triangle = [0] * n

    for g in range(n):
        # define a row and fill first and last index with 1
        n_row = [0] * (g+1)
        n_row[0] = 1
        n_row[len(n_row) - 1] = 1

        for r in range(1, g):
            if r > 0 and r < len(n_row):
                a = pascal_triangle[g - 1][r]
                b = pascal_triangle[g - 1][r - 1]
                new_row[r] = a + b

        pascal_triangle[g] = n_row

    return pascal_triangle
