#!/usr/bin/python3
""" A module to define an inherited class-checking function. """


def inherits_from(obj, a_class):
    """Checks if an obj is an inherited instance of a class.
    Args:
        obj (any): object to check
        a_class (type): class type to be matched to obj
        Returns: True if obj is an inherited instance of a_class
        otherwise, returns false.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
