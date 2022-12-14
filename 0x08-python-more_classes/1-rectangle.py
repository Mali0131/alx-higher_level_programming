#!/usr/bin/python3
""" A class that defines a rectangle"""


class Rectangle:
    """ Rectangle class"""

    def __init__(self, width=0, height=0):
        """initialize the rectangle
        Args:
            width: Width of the rectangle
            height: Height of the rectangle
        raise:
            TypeError: if the passed value is not integer
            ValueError: if value passed is less than 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ makes the width property private"""

        return self.__width

    @width.setter
    def width(self, value):
        """Set the value for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """make the height prvate"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
