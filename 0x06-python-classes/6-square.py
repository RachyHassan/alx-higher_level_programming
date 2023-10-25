#!/usr/bin/python3
""" A module to define a class Square. """


class Square:
    """ A class to represent a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new instance of the square class. """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Return the size in int. """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Handle type and value errors. """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """print the position. """
        return (self.__position)

    @position.setter
    def position(self.value):
        """ Handle type and value errors. """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tupple of 2 positive integers")
        self.__position = value

    def area(self):
        """ print the square. """
        return (self.__size * self.__size)

    def my_print(self):
        """ print the size and position. """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
