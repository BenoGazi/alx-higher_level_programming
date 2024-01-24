#!/usr/bin/python3
"""Square class Definition."""
class Square:
    """Square."""

    def __init__(self, size=0):
        """Initialise class square instance
        Args:
        size (init): The size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square's area."""
        return (self.__size * self.__size)
