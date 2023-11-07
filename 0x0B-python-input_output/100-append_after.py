#!/usr/bin/python3
""" A function that inserts a text file. """


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a specific string.
            filename (str) : name of file
            search_string (str) : string to search for
            new_string (str) : string to be added.
    """
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
