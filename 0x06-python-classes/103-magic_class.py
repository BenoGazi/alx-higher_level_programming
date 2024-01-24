#!/usr/bin/python3
"""Define a magic class matching
one byte code
"""
import math
class MagicClass:
    """Circle of magic"""
    def __init__(self, radius=0):
        """magic class init
        Arg:
            radius (float or int): The radius of the new Magic Class.
        """
        if not isinstance(radius, (int, float)):
            raise  TypeError("radius must be a number")
        self.__radius = radius
    def area(self):
        """Return the area of the Magic Class."""
        return self.__radius ** 2 * math.pi
    def circumference(self):
        """Circumference of the Magic Class"""
        return 2 * math.pi * self.__radius
