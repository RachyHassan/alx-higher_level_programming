#!/usr/bin/python3
""" A function that defines a python class to JSON. """


def class_to_json(obj):
    return obj.__dict__
