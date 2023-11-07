#!/usr/bin/python
""" A function that returns an object from JSON. """
import json


def from_json_string(my_str):
    """ Returns an object represented by a JSON string. """
    return (json.loads(my_str))
