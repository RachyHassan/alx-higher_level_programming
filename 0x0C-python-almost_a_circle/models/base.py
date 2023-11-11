#!/usr/bin/python3
""" A module to define a base model class. """
import csv
import json


class Base:
    """ Base class represents the foundation for all
    other classes.
    _nb_object (int): Number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize a new base with argument id.
        id (int): identity of the new base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON serialization of a list
        of dictionaries.
            list_dictionaries (list): a list of
            dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        to_json = json.dumps(list_dictionaries)

        return (to_json)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON serialization of a list
                list_objs (list): List of inherited Base
                instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for n in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the deserialization of a list
        of dictionaries.
            json_string (str): a JSON string representation of
            a list of dictionaries.
                This returns an empty list if json_string is None
            or empty. Otherwise, it returns the list repreented by
            json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantiated from a dictionary of attributes.
            Args:
                **dictionary (dict): key/value pairs of
                attributes to initialize.
        """
        if dictionary and dictionary != []:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return (new)

    @classmethod
    def load_from_file(cls):
        """ Return a list of classes instantiated from a file of JSON strings.
        '<cls.__name__>.json'.
                If the file does not exist, it returns an empty list.
                Otherwise, it returns a list of instantiated classes.
        """
        file = str(cls.__name__) + ".json"
        try:
            with open(file, "r") as newfile:
                list_dicts = Base.from_json_string(newfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
