#!/usr/bin/python3
""" A function defining a pascal triangle. """


def pascal_triangle(n):
    """ Representation of a pascal triangle with size n.
        Returns: a list of list of int
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        t = triangles[-1]
        tmp = [1]
        for i in range(len(t) - 1):
            tmp.append(t[i] + t[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
