#!/usr/bin/python3
"""Class definition for square."""
class Square:
    """Represent a square."""
    def __init__(self, size):
        """New Square.
        Args:
            size (int): The ize of the new square.
        """
        self.size = size
    @property
    def size(self):
        """Get or set the size of square(current)."""
        return self.__size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """Return current square area."""
        return self.__size * self.__size
    def my_print(self):
        """print the block of the square."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print ("")
            if self.__size == 0:
                print("")
