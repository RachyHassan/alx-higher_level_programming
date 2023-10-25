#!/usr/bin/python3
"""A square module to define the Square class."""


class Square:
    """ A class to represent a Square."""
    def __init__(self, size=0):
        """ Initialize the instance size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
    self.__size = size

    def area(self):
        return (self.__size * self.__size)
