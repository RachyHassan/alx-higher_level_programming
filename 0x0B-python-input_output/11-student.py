#!/usr/bin/python3
""" Define a class Student. """


class Student:
    """ Representation of Student. """

    def __init__(self, first_name, last_name, age):
        """Initialize student with args:
            first_name (str)
            last_name (str)
            age (int)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Dictionary representation of a student.
            attrs (list) is a list of attributes
        """
        if (isinstance(attrs) == list and
                all(isinstance(element) == str for element in attrs)):
            return {j: getattr(self, j) for
                    j in attrs if hasattr(self, j)}
        return self.__dict__

    def reload_from_json(self, json):
        """ Replace all attributes of Student
            Args: Json (dict)
        """
        for i, j n json.items():
            setattr(self, i, j)
