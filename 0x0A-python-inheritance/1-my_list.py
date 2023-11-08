#!/usr/bin/python3
""" A class list MyList. """


class MyList(list):
    """ Implement sorted list for the class. """

    def print_sorted(self):
        """ Print sorted list in ascending order. """
        print(sorted(self))
