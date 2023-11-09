#!/usr/bin/python3
""" A module that adds attributes to objects. """


def add_attribute(obj, att, value):
    """ A function to add a new attribute.
    Args:
        obj (any): object to add an attribute to
        att (str): name of the attribute to be added
        value (any): value of att
    Raise: TypeError if attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
