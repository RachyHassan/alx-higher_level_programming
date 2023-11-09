#!/usr/bin/python3
"""A module to define a class BaseGeometry. """


class BaseGeometry:
    """ A class to represent base geometry. """

    def area(self):
        """ Area is not implemented. """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ a function to validate a parameter as an integer.
        Args:
            name (str): name of the parameter to be validated
            value (int): parameter to validate.
        Raises:
            TypeError: if value is not an int
            ValueError: if value <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(value))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if type(name) != str:
            raise TypeError("{} must be a string".format(name))
