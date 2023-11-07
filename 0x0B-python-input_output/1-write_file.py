#!/usr/bin/python3
""" A function that writes a string to a text file (UTF8). """


def write_file(filename="", text=""):
    """ Write a string to the text file.
    Args:
        filename (str): name of the file.
        text (str): text to be written.
        Return: Number of characters to be written.
    """

    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
