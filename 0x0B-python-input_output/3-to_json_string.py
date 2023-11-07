#!/usr/bin/python3
""" A function that converts a string to JSON. """
import json


def to_json_string(my_obj):
    """ Returns the JSON representation of the string. """
    return (json.dumps(my_obj))
