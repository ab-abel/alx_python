#!/usr/bin/python3
"""
This is a module design to explore basic concept of class
"""

class Square:
    """
    This module initilaize a square methond and check if the value is of type int or less than 0 
    """
    def __init__(self, size=0):
        if type(size) != int:
            try:
                raise TypeError("size must be an integer")
            except TypeError as te:
                print(te)
        if size<=0:
            try:
                raise ValueError("size must be >= 0")
            except ValueError as var:
                print(var)
        self.__size = size
