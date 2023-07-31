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
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value ** 2

    def area(self):
        size = self.__size
        return size


my_square = Square(89)
print(my_square.size)
# print(my_square.area())
# my_square.size = 33
# print(my_square.size)
# print(my_square.area())