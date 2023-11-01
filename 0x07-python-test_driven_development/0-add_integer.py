#!/usr/bin/python3
""" A function that adds two integers. """


def add_integer(a, b=98):
    """ Returns the addition of a and b.
    A type error is raised if a or b is not a n integer
    or a float number.
    If a or b is a float, it should be casted to an integer
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer.")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer.")
    a = int(a)
    b = int(b)

    return a + b
