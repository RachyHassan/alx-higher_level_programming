#!/usr/bin/python3
""" A module to define a rectangle. """


class Rectangle:
    """ A class to represent a rectangle. """

    def __init__(self, width=0, height=0):
        """ initializing a new Rectangle with arguments width
        and height.
        Args:
        width (int): the width of the rectangle.
        height (int): the height of the new rectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Set 'width' to retrieve from rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ set 'height' to retrieve from rectangle. """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
