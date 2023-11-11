#!/usr/bin/python3
""" A module to represent a Square. """
from rectangle import Rectangle


class Square(Rectangle):
    """ A class Square that inherits from Rectangle. """

    def __init__(self, size, x=0, y=0, id=None):
        """ A constructor for the square class. """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """ size setter. """
        self.width = value
        self.height = value

    def __str__(self):
        """ A str representation to override str() """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                            self.x,
                                            self.y, self.width)

    def update(self, *args, **kwargs):
        """ Assigns arguments to attributes based
        on position.
        """
        if args:
            attributes = ["id", "size", "x", "y"]

            for i, attr in enumerate(attributes):
                if i < len(args):
                    setattr(self, attr, args[i])
        elif len(kwargs) > 0:
            keys = ["id", "size", "x", "y"]

            for i, attr in enumerate(keys):
                if attr in kwargs:
                    setattr(self, attr, kwargs[attr])

    def to_dictionary(self):
        """ Returns the dictionary Representation
        of the square. """
        square_dict = {
                    "id": self.id,
                    "x": self.x,
                    "size": self.width,
                    "y": self.y
                    }
        return (square_dict)

if __name__ == "__main__":

    s1 = Square(10, 2, 1)
    print(s1)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(s1 == s2)
