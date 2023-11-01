#!/usr/bin/python3
""" Defines a square printing function. """


def print_square(size):
    """ Prints a square using the # character.
    Args:
    Size (int): the height and width of the square.
    TypeError: if size is not an integer
    ValueError: if size <= 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size == 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
