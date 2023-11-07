#!/usr/bin/python3
""" A function that reads a text file. """


def read_file(filename=""):
    """ print out the content of the text file to stdout."""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
