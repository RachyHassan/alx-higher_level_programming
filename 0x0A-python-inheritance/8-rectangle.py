#!/usr/bin/python3
""" A module to define a class Rectangle inherited from BaseGeometry. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A class to represent a rectangle. """

    def __init__(self, width, height):
        """ Initialize a new rectangle.
        Args:
            width (int)
            height (int)
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
