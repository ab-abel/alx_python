#!/usr/bin/python3
"""
Module calculate the area of a square
"""


class Square:
    """
    this class uses the getter to return the area from
    the square method
    """
    def __init__(self, size=0):
        self.__size = size

    def size(self, value):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value ** 2

    def area(self):
        return self.__size
