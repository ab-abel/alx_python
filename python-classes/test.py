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
        self.set_size(size)
        self.size = self.get_size()

    def set_size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def get_size(self):
        return self.__size

    def area(self):
        return self.size ** 2