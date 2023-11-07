#!/usr/bin/python3
"""A function to append in a file. """


def append_write(filename="", text=""):
    """ Append a string to the end of a text file.
    Args:
        Filename (str)
        text (str)
        Return: Number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
