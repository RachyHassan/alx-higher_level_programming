#!/usr/bin/python3
""" A module to define a rectangle. """


class Rectangle:
    """ A class to represent a rectangle. """

    def __init__(self, width=0, height=0):
        """ Initializing a new rectangle with arguments width and height.
        Args:
        width (int): the width of the rectangle
        height (int): the height of the rectangle. """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Set 'width' to retrieve from rectangle. """
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
            raise TypeError("height must be a rectangle")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of a rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """ Return the printable representation of the rectangle. """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """ Returns the string representation of a rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
