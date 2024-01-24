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
        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise  TypeError("radius must be a number")
        self.__radius = radius
        def area(self):
            """Return the area of the Magic Class."""
            return se.f__radius ** 2 * math.pi
        def circumference(self):
            """Circumference of the Magic Class"""
            return 2 * math.pi * self__radius
