#!/usr/bin/python3
""" A function that defines a class. """


def is_kind_of_class(obj, a_class):
    """check if an object is an instance or inherited
    instance of a class.
    Args:
        obj (any): object to check.
        a_class (type): class to be matched to obj.
        Returns: true if obj is an instance or inherited instance
        of a_class. Otherwise, false.
    """
    if isinstance(obj, a_class):
        return True
    return False
