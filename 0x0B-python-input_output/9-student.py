#!/usr/bin/python3
""" Defines a class Student. """


class Student:
    """ Representation of a student. """

    def __init__(self, first_name, last_name, age):
        """ Initialize the class with args:
            first_name (str)
            last_name (str)
            age (int)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ return the dictionary representation of Student. """
        return self.__dict__
