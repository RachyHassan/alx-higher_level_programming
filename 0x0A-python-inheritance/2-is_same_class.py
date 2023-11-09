#!/usr/bin/python3
""" A function that checks the instance of a class. """


def is_same_class(obj, a_class):
    """ Check if an object is exactly an instance of a given class.
    Args:
        obj (any): object to be checked.
        a_class (type): class to be matched to obj.
        Returns: true if obj is an exact instance of a_class.
        else, return false.
    """
    if type(obj) == a_class:
        return True
    return False
