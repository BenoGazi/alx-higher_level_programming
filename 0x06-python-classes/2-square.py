#!/usr/bin/python3

"""Definition of Square class."""

class: Square:
    """Square class."""

    def __init__(self, size = 0):
        """New Square

        args:
            size (int: New square size).
        """
        if not instance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("size must greater than 0")
        self.__size = size

