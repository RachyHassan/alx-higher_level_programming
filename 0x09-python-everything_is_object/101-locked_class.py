#!/usr/bin/python3
"""Defines a locked class. """


class LockedClass:
    """
    This prevents the user from dynamically
    creating new instance attributes.
    Escept if new instance attribute is called
    first_name.
    """
    __slots__ = ["first_name"]
