#!/usr/bin/python3
""" Define a class Student. """


class Student:
    """ Representation of a student. """

    def __init__(self, first_name, last_name, age):
        """ Initialize class student with args:
            first_name (str)
            last_name (str)
            age (int)
        """
        self.first_name = first_name
        self.last_nme = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Dictionary representation of Student.
            attrs (list): is a list of strings
            that represents the attributes
        """
        if (isinstance(attrs) == list and
                all(isinstance(element) == str for element in attrs)):
            return {j: getattr(self, j) for
                    j in attrs if hasattr(self, j)}
        return self.__dict__
