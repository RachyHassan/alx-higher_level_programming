#!/usr/bin/python3
""" A module for a Rectangle class. """
from models.base import Base


class Rectangle(Base):
    """ A class Rectangle that inherits from Base. """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter. """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter. """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height setter. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """ x getter. """
        return self.__x

    @x.setter
    def x(self, value):
        """x setter """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """y getter. """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ The area of the rectangle. """
        area = self.width * self.height
        return (area)

    def display(self):
        """ Prints the sixe of the rectangle using #. """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ Return the print() and str() representation
        of rectangle. """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """ Assign arguments to attributes based on position.
            Assign kwargs only if args is not passed. """
        if args:
            attributes = ["id", "width", "height", "x", "y"]

            for i, attr in enumerate(attributes):
                if i < len(args):
                    setattr(self, attr, args[i])
        elif len(kwargs) > 0:
            keys = ["id", "width", "height", "x", "y"]

            for i, attr in enumerate(keys):
                if attr in kwargs:
                    setattr(self, attr, kwargs[attr])

    def to_dictionary(self):
        """ Represents a dictionary
        representation of a rectangle. """
        rect_dict = {
                    "x": self.x,
                    "width": self.width,
                    "id": self.id,
                    "height": self.height,
                    "y": self.y
                    }
        return (rect_dict)
