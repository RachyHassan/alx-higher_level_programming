#!/usr/bin/python3
""" A module to define a base model class. """
import csv
import json
import turtle


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
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = []
                for obj in list_objs:
                    list_dicts.append(obj.to_dictionary())
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
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return (dummy)

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
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ write a CSV serialization of a list of objects. """
        filename = "{}.csv".format(cls.__name__)

        with open(filename, "w") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                written_file = csv.DictWriter(csvfile, fieldnames=field_names)

            for obj in list_objs:
                written_file.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Returns a list of classes from a CSV file. """
        filename = "{}.csv".format(cls.__name__)

        try:
            with open(filename, "r") as csv_file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                dicts = csv.DictReader(csv_file, fieldnames=fieldnames)

                list_of_instances = []

                for l in dicts:
                    converted_list = {}
                    for key, value in l.items():
                        converted_list[key] = int(value)

                    list_of_instances.append(cls.create(**converted_list))

                return list_of_instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Opens a window and draws all the rectangles and squares. """
        turt = turtle.Turtle()

        turt.screen.bgcolor("#FF1493")

        turt.pensize(4)

        turt.shape("turtle")

        for rec in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rec.x, rec.y)
            turt.down()

            for r in range(2):
                turt.forward(rec.width)
                turt.left(90)
                turt.forward(rec.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#DA70D6")

        for s in list_squares:
            turt.showturtle()
            turt.up()
            turtle.goto(s.x, s.y)
            turt.down()

            for r in range(2):
                turt.forward(s.width)
                turt.left(90)

                turt.forward(s.height)

                turt.left(90)
            turt.hideturtle()
        turtle.exitonclick()
