#!/usr/bin/python3
""" A module to define a class Rectangle inherited from BaseGeometry. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class to represent a rectangle. """

    def __init__(self, width, height):
        """Initialize a new Rectangle.
        Args:
            width (int)
            height (int)
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ A function to return the area of the rectangle. """
        return (self.width * self.height)

    def __str__(self):
        """ Returns the print() and str() representations of the rectangle. """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return (string)
