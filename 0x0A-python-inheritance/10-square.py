#!/usr/bin/python3
""" A module to define a subclass Square under Rectangle. """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A class to represent a square. """

    def __init__(self, size):
        """ Initialize a new square.
        Args:
            size (int)
        """
        self.integer_validator("size", size)
        self.__size = size
