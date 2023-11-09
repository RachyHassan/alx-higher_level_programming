#!/usr/bin/python3
"""A module to define a class MyInt that inherits from int. """


class MyInt(int):
    """ nvert int operators == and !=. """

    def __eq__(self, value):
        """ override == operator with != behavior."""
        return (self.real != value)

    def __ne__(self, value):
        """override != with == behavior. """
        return (self.real == value)
